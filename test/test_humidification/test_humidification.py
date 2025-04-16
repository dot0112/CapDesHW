"""
Vin -> 5V
GND -> GND
EN -> TR-C

TR-E -> GND
TR-B -> GPIO 21 (Pin 40)
"""

import RPi.GPIO as g
import time

HUMIDIFICATION = 21

g.setmode(g.BCM)
g.setup(HUMIDIFICATION, g.OUT)
g.output(HUMIDIFICATION, g.HIGH)


def toggleHumidification():
    g.output(HUMIDIFICATION, g.LOW)
    time.sleep(0.1)
    g.output(HUMIDIFICATION, g.HIGH)


while True:
    key = input("1 to Toggle Mode, x to Exit: ")
    if key == "1":
        print("Toggle Mode")
        toggleHumidification()
    elif key == "x":
        print("exit")
        break
