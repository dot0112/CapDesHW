from .module import Module
from main.models import singleton
import adafruit_sht31d
import board


@singleton
class THSensor(Module):
    def __init__(self):
        self.i2c = board.I2C()
        self.sensor = adafruit_sht31d.SHT31D(self.i2c)
        self.data = [0.0, 0.0]

    def activate(self):
        self.data = [self.sensor.temperature, self.sensor.relative_humidity]

    def deactivate(self):
        pass
