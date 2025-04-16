"""
TXD3 -> GPIO 4 (Pin 7)
RXD3 -> GPIO 5 (Pin 29)
"""

import serial
import time
import RPi.GPIO as g

mod = serial.Serial(port="/dev/ttyAMA3", baudrate=9600)

g.setmode(g.BCM)

while True:
    mod.write(b"\xff")
    time.sleep(0.01)
