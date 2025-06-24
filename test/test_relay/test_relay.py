"""
INPUT(-) -> GND
INPUT(+) -> GPIO 18 (Pin 12)
"""

import RPi.GPIO as g

RELAYPIN = 1

g.setmode(g.BCM)
g.setup(RELAYPIN, g.OUT)

while True:
    key = input("press 0 to OFF, 1 to On, x to exit: ")
    if key == "0":
        g.output(RELAYPIN, False)
    elif key == "1":
        g.output(RELAYPIN, True)
    elif key == "x":
        g.output(RELAYPIN, False)
        break
