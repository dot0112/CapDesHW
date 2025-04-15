import serial
import time
import RPi.GPIO as g

mod = serial.Serial(port="/dev/ttyAMA3", baudrate=9600)

g.setmode(g.BCM)
# for pin in range(2, 28):
#     print(pin, end=" ")
#     try:
#         g.setup(pin, g.OUT)
#         g.output(pin, g.LOW)
#     except Exception as e:
#         print(f"{e}")


while True:
    mod.write(b"\xff")
    time.sleep(0.01)
