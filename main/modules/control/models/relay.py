from .module import Module
from main.models import singleton
from dotenv import load_dotenv
import RPi.GPIO as g
import os


@singleton
class Relay(Module):
    def __init__(self):
        load_dotenv()
        self.RELAY = int(os.getenv("PIN_RELAY"))
        g.setup(self.RELAY, g.output)

    def activate(self):
        g.output(self.RELAY, g.HIGH)

    def deactivate(self):
        g.output(self.RELAY, g.LOW)
