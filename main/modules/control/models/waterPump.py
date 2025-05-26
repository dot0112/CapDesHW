from .module import Module
from main.models import singleton
from dotenv import load_dotenv
import RPi.GPIO as g
import os


@singleton
class WaterPump(Module):
    def __init__(self):
        load_dotenv()
        self.WATERPUMP_A = int(os.getenv("PIN_WATERPUMP_A"))
        self.WATERPUMP_B = int(os.getenv("PIN_WATERPUMP_B"))
        g.setup(self.WATERPUMP_A, g.OUT)
        g.setup(self.WATERPUMP_B, g.OUT)
        g.output(self.WATERPUMP_B, g.LOW)

    def activate(self):
        g.output(self.WATERPUMP_A, g.HIGH)

    def deactivate(self):
        g.output(self.WATERPUMP_A, g.LOW)
