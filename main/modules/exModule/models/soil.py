from .module import Module
from dotenv import load_dotenv
from threading import Thread
from datetime import datetime
import RPi.GPIO as g
import serial
import time
import os


class Soil(Thread, Module):

    DATAMOD = [
        [0x02, 0x03, 0x00, 0x00, 0x00, 0x01, 0x84, 0x39],  # moist
        [0x02, 0x03, 0x00, 0x01, 0x00, 0x01, 0xD5, 0xF9],  # temp
        [0x02, 0x03, 0x00, 0x02, 0x00, 0x01, 0x25, 0xF9],  # ec
        [0x02, 0x03, 0x00, 0x03, 0x00, 0x01, 0x74, 0x39],  # ph
    ]

    TIMEOUT = 100

    def __init__(self):
        Thread.__init__(self)
        load_dotenv()
        self.status = False
        self.data = [0.0, 0.0, 0.0, 0.0]
        self.SoilDRE = int(os.getenv("PIN_SOIL"))
        self.mod = serial.Serial(
            port="/dev/ttyAMA5",
            baudrate=2400,
            bytesize=serial.EIGHTBITS,
            parity=serial.PARITY_NONE,
            stopbits=1,
        )
        g.setup(self.SoilDRE, g.OUT)
        g.output(self.SoilDRE, 0)

    def getModVal(self, val):
        self.mod.reset_input_buffer()
        self.mod.reset_output_buffer()
        startTime = 0
        byteCount = 0
        buf = bytearray(7)

        g.output(self.SoilDRE, 1)
        time.sleep(0.01)
        self.mod.write(bytes(self.DATAMOD[val]))
        self.mod.flush()
        g.output(self.SoilDRE, 0)

        startTime = int(time.time() * 1000)
        while int(time.time() * 1000) - startTime <= self.TIMEOUT:
            if self.mod.in_waiting > 0 and byteCount < len(buf):
                byte = self.mod.read(1)
                buf[byteCount] = int.from_bytes(byte)
                byteCount += 1

        return int(buf[3] << 8 | buf[4])

    def activate(self):
        print("[exModule] soil activate")
        for i in range(4):
            self.data[i] = self.getModVal(i) * (0.1 if i != 2 else 1)
            time.sleep(0.1)
        self.moduleRecord.soil = datetime.now()

    def deactivate(self):
        pass

    def run(self):
        while True:
            self.controlFlag.soilEvent.wait()

            self.activate()
            (
                    self.sensorData.soilHumi,
                    self.sensorData.soilTemp,
                    self.sensorData.soilEC,
                    self.sensorData.soilPH,
            ) = self.data

            self.controlFlag.soil = False