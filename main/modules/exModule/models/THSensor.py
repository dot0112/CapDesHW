from .module import Module
from models import singleton
from threading import Thread
from datetime import datetime
import adafruit_sht31d
import board
import time
import os


@singleton
class THSensor(Thread, Module):
    def __init__(self):
        Thread.__init__(self)
        self.i2c = board.I2C()
        self.sensor = adafruit_sht31d.SHT31D(self.i2c)
        self.data = [0.0, 0.0]

    def activate(self):
        self.data = [self.sensor.temperature, self.sensor.relative_humidity]
        self.moduleRecord.THSensor = datetime.now()

    def deactivate(self):
        pass

    def run(self):
        while True:
            if self.controlFlag.THSensor:
                self.activate()
                (self.sensorData.temp, self.sensorData.humi) = self.data
            time.sleep(1)
