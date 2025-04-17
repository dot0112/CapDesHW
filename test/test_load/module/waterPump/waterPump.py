import RPi.GPIO as g

A_1A = 23
A_1B = 24
g.setmode(g.BCM)
g.setup(A_1A, g.OUT)
g.setup(A_1B, g.OUT)
g.output(A_1B, g.LOW)


def actWaterPump(_, e):
    if e == 0:
        g.output(A_1A, g.LOW)
    elif e == 1:
        g.output(A_1A, g.HIGH)
