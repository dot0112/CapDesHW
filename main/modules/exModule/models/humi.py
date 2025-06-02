from .module import Module
from models import singleton
from dotenv import load_dotenv
from threading import Thread
from datetime import datetime
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
        self.moduleRecord.humi = datetime.now()

    def deactivate(self):
        self.switchHumidification()

    def run(self):
        while True:
            if self.controlFlag.humi != self.status == True:
                self.activate()
                self.status = not self.status
                self.activate() if self.status else self.deactivate()

            time.sleep(1)
