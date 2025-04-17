import adafruit_sht31d
import board
import time

i2c = board.I2C()
sensor = adafruit_sht31d.SHT31D(i2c)


def actTemHum(dataBuf, e):
    if e == 0:
        return
    dataBuf["temp"] = sensor.temperature
    dataBuf["humi"] = sensor.relative_humidity
    return
