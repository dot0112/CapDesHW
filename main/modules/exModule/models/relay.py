from .module import Module
from models import singleton
from dotenv import load_dotenv
from threading import Thread
from datetime import datetime
import RPi.GPIO as g
import time
import os


@singleton
class Relay(Thread, Module):
    def __init__(self):
        Thread.__init__(self)
        load_dotenv()
        self.status = False
        self.RELAY = int(os.getenv("PIN_RELAY"))
        g.setup(self.RELAY, g.OUT)
        g.output(self.RELAY, g.LOW)

    def activate(self):
        g.output(self.RELAY, g.HIGH)
        self.moduleRecord.relay = datetime.now()

    def deactivate(self):
        g.output(self.RELAY, g.LOW)

    def run(self):
        while True:
            if self.controlFlag.relay != self.status:
                self.status = not self.status
                self.activate() if self.status else self.deactivate()

            time.sleep(1)
