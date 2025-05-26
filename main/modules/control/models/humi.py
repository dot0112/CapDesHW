from .module import Module
from main.models import singleton
from dotenv import load_dotenv
import RPi.GPIO as g
import time
import os


@singleton
class Humi(Module):
    def __init__(self):
        load_dotenv()
        self.data = []
        self.HUMIDIFICATION = int(os.getenv("PIN_HUMI"))
        g.setup(self.HUMIDIFICATION, g.OUT)
        g.output(self.HUMIDIFICATION, g.HIGH)

    def switchHumidification(self):
        g.output(self.HUMIDIFICATION, g.LOW)
        time.sleep(0.1)
        g.output(self.HUMIDIFICATION, g.HIGH)

    def activate(self):
        self.switchHumidification()

    def deactivate(self):
        self.switchHumidification()
