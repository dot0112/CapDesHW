from .module import Module
from dotenv import load_dotenv
from threading import Thread
from datetime import datetime
import RPi.GPIO as g
import time
import os


class Relay(Thread, Module):
    def __init__(self):
        Thread.__init__(self)
        load_dotenv()
        self.status = False
        self.RELAY = int(os.getenv("PIN_RELAY"))
        g.setup(self.RELAY, g.OUT)
        g.output(self.RELAY, g.LOW)

    def activate(self):
        print("[exModule] relay activate")
        g.output(self.RELAY, g.HIGH)
        self.moduleRecord.relay = datetime.now()

    def deactivate(self):
        g.output(self.RELAY, g.LOW)

    def run(self):
        while True:
            self.controlFlag.relayEvent.wait()

            self.status = not self.status
            self.activate() if self.status else self.deactivate()

            self.controlFlag.relay = False
