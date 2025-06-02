from .module import Module
from models import singleton
from dotenv import load_dotenv
from threading import Thread
from datetime import datetime
import RPi.GPIO as g
import time
import os


@singleton
class WaterPump(Thread, Module):
    def __init__(self):
        Thread.__init__(self)
        load_dotenv()
        self.status = False
        self.WATERPUMP_A = int(os.getenv("PIN_WATERPUMP_A"))
        self.WATERPUMP_B = int(os.getenv("PIN_WATERPUMP_B"))
        g.setup(self.WATERPUMP_A, g.OUT)
        g.setup(self.WATERPUMP_B, g.OUT)
        g.output(self.WATERPUMP_B, g.LOW)

    def activate(self):
        g.output(self.WATERPUMP_A, g.HIGH)
        self.moduleRecord.waterPump = datetime.now()

    def deactivate(self):
        g.output(self.WATERPUMP_A, g.LOW)

    def run(self):
        while True:
            if self.controlFlag.waterPump != self.status:
                self.status = not self.status
                self.activate() if self.status else self.deactivate()
            time.sleep(1)
