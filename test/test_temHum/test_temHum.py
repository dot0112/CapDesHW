"""
Vin -> 5V
GND -> GND
SCL -> GPIO 3 (Pin 5)
SDA -> GPIO 2 (Pin 3)
"""

import adafruit_sht31d
import board
import time

i2c = board.I2C()
sensor = adafruit_sht31d.SHT31D(i2c)

print("----------------------------")

while True:
    print(f"TEMP: {sensor.temperature} / HUMI: {sensor.relative_humidity}", end="\r")
    time.sleep(1)
