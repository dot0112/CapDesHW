import RPi.GPIO as g

RELAYPIN = 18

g.setmode(g.BCM)
g.setup(RELAYPIN, g.OUT)


def actRelay(_, e):
    g.output(RELAYPIN, e)
