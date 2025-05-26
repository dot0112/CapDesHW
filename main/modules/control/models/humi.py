from .module import Module
from main.models import singleton
from dotenv import load_dotenv
from threading import Thread
import RPi.GPIO as g
import time
import os


@singleton
class Humi(Thread, Module):
    def __init__(self):
        Thread.__init__(self)
        load_dotenv()
        self.status = False
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
        pass

    def run(self):
        while True:
            if self.controlFlag.humi != self.status == True:
                self.activate()
                self.status = not self.status
            time.sleep(1)
