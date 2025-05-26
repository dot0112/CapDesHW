"""
SoilSensor-Black -> GND
SoilSensor-Brown -> SMPS-V+
SoilSensor-Blue -> MAX485-B
SoilSensor-Yellow -> MAX485-A

MAX485-VCC -> 3.3V
MAX485-GND -> GND

MAX485-DI -> GPIO 4 (Pin 7)
MAX485-DE -> GPIO 17 (Pin 11)
MAX485-RE -> GPIO 27 (Pin 13)
MAX485-RO -> GPIO 5 (Pin 29)
"""

### init ###

import time
import os
import serial
import RPi.GPIO as g

BUF_SIZE = 20
TIMEOUT = 100

MOIST = 0
TEMP = 1
EC = 2
PH = 3

DE = 26
RE = 26

dataMod = [
    [0x02, 0x03, 0x00, 0x00, 0x00, 0x01, 0x84, 0x39],  # moist
    [0x02, 0x03, 0x00, 0x01, 0x00, 0x01, 0xD5, 0xF9],  # temp
    [0x02, 0x03, 0x00, 0x02, 0x00, 0x01, 0x25, 0xF9],  # ec
    [0x02, 0x03, 0x00, 0x03, 0x00, 0x01, 0x74, 0x39],  # ph
]

buf = None
mod = None


### function ###
def GetModVal(val):
    global buf
    mod.reset_input_buffer()
    mod.reset_output_buffer()
    startTime = 0
    byteCount = 0
    buf = bytearray(7)

    g.output(DE, 1)
    g.output(RE, 1)
    time.sleep(0.01)
    mod.write(bytes(dataMod[val]))
    mod.flush()
    g.output(DE, 0)
    g.output(RE, 0)

    print(" " * 50, end="")
    print(f"\r({val})Response in HEX: ", end="")
    startTime = int(time.time() * 1000)
    while int(time.time() * 1000) - startTime <= TIMEOUT:
        if mod.in_waiting > 0 and byteCount < len(buf):
            byte = mod.read(1)
            print(f"{byte.hex()} ", end="")
            buf[byteCount] = int.from_bytes(byte)
            byteCount += 1

    return int(buf[3] << 8 | buf[4])


def main():
    ### setup ###
    global mod
    os.system("clear")
    mod = serial.Serial(
        port="/dev/ttyAMA5",
        baudrate=2400,
        bytesize=serial.EIGHTBITS,
        parity=serial.PARITY_NONE,
        stopbits=1,
    )

    g.setmode(g.BCM)
    g.setup(DE, g.OUT)
    g.setup(RE, g.OUT)
    print("Ready..")

    ### loop ###
    while True:
        val_MOIST = GetModVal(MOIST) * 0.1
        time.sleep(0.1)
        val_TEMP = GetModVal(TEMP) * 0.1
        time.sleep(0.1)
        val_EC = GetModVal(EC)
        time.sleep(0.1)
        val_PH = GetModVal(PH) * 0.1
        time.sleep(0.1)

        os.system("clear")
        print(
            f"""Moisture: {val_MOIST:.2f} %
-----
Temperature: {val_TEMP:.2f} *C
-----
EC: {val_EC:.2f} us/cm
-----
PH: {val_PH:.2f} ph
----"""
        )


if __name__ == "__main__":
    main()
