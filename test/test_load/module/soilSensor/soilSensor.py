import time
import serial
import RPi.GPIO as g

BUF_SIZE = 20
TIMEOUT = 100

MOIST = 0
TEMP = 1
EC = 2
PH = 3

DE = 17
RE = 27

dataMod = [
    [0x02, 0x03, 0x00, 0x00, 0x00, 0x01, 0x84, 0x39],  # moist
    [0x02, 0x03, 0x00, 0x01, 0x00, 0x01, 0xD5, 0xF9],  # temp
    [0x02, 0x03, 0x00, 0x02, 0x00, 0x01, 0x25, 0xF9],  # ec
    [0x02, 0x03, 0x00, 0x03, 0x00, 0x01, 0x74, 0x39],  # ph
]

buf = None
mod = serial.Serial(
    port="/dev/ttyAMA3",
    baudrate=2400,
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=1,
)

g.setmode(g.BCM)
g.setup(DE, g.OUT)
g.setup(RE, g.OUT)


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

    startTime = int(time.time() * 1000)
    while int(time.time() * 1000) - startTime <= TIMEOUT:
        if mod.in_waiting > 0 and byteCount < len(buf):
            byte = mod.read(1)
            buf[byteCount] = int.from_bytes(byte)
            byteCount += 1

    return int(buf[3] << 8 | buf[4])


def actSoilSensor(dataBuf, e):
    if e == 0:
        return
    dataBuf["soilTemp"] = GetModVal(TEMP) * 0.1
    dataBuf["soilHumi"] = GetModVal(MOIST) * 0.1
    dataBuf["soilEC"] = GetModVal(EC)
    dataBuf["soiilPH"] = GetModVal(PH) * 0.1

    return
