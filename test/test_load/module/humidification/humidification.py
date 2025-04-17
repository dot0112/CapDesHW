import RPi.GPIO as g
import time

HUMIDIFICATION = 21

g.setmode(g.BCM)
g.setup(HUMIDIFICATION, g.OUT)
g.output(HUMIDIFICATION, g.HIGH)

state = 0


def toggleHumidification():
    g.output(HUMIDIFICATION, g.LOW)
    time.sleep(0.1)
    g.output(HUMIDIFICATION, g.HIGH)


def actHumidification(_, e):
    global state
    if e != state:
        state = e
        toggleHumidification()
