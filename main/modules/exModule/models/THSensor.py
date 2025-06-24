from .module import Module
from threading import Thread
from datetime import datetime
import adafruit_sht31d
import board
import time
import os


class THSensor(Thread, Module):
    def __init__(self):
        Thread.__init__(self)
        try:
            self.i2c = board.I2C()
            self.sensor = adafruit_sht31d.SHT31D(self.i2c)
            self.data = [0.0, 0.0]
        except Exception as e:
            print(e)

    def activate(self):
        print("[exModule] THSensor activate")
        self.data = [self.sensor.temperature, self.sensor.relative_humidity]
        self.moduleRecord.THSensor = datetime.now()

    def deactivate(self):
        pass

    def run(self):
        while True:
            self.controlFlag.THSensorEvent.wait()

            self.activate()
            (self.sensorData.temp, self.sensorData.humi) = self.data

            self.controlFlag.THSensor = False
            
