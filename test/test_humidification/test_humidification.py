import RPi.GPIO as g

HUMIDIFICATION = 21

g.setmode(g.BCM)
g.setup(HUMIDIFICATION, g.OUT)
g.output(HUMIDIFICATION, g.LOW)

while True:
    key = input("1 to On, 0 to Off, x to Exit: ")
    if key == "1":
        g.output(HUMIDIFICATION, g.HIGH)
    elif key =="0":
        g.output(HUMIDIFICATION, g.LOW)
    elif key =="x":
        break
    
g.output(HUMIDIFICATION, g.LOW)

