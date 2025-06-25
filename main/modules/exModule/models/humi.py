from .module import Module
from dotenv import load_dotenv
from threading import Thread
from datetime import datetime
import RPi.GPIO as g
import time
import os


class Humi(Thread, Module):
    def __init__(self):
        Thread.__init__(self)
        load_dotenv()
        self.status = False
        self.HUMIDIFICATION = int(os.getenv("PIN_HUMI"))
        g.setup(self.HUMIDIFICATION, g.OUT)
        g.output(self.HUMIDIFICATION, g.LOW)

    def activate(self):
        print("[exModule] humi activate")
        g.output(self.HUMIDIFICATION, g.HIGH)
        self.moduleRecord.humi = datetime.now()

    def deactivate(self):
        g.output(self.HUMIDIFICATION, g.LOW)

    def clear(self):
        g.output(self.HUMIDIFICATION, g.LOW)

    def run(self):
        while True:
            self.controlFlag.humiEvent.wait()

            self.status = not self.status
            self.activate() if self.status else self.deactivate()

            self.controlFlag.humi = False
