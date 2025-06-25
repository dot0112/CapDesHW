from .module import Module
from threading import Thread
from datetime import datetime
import adafruit_dht
import board
import threading
import time


class THSensor(Thread, Module):
    def __init__(self):
        Thread.__init__(self)
        try:
            self.sensor = adafruit_dht.DHT11(board.D2, use_pulseio=True)
            self.data = [100.0, 100.0]
            self.lock = threading.Lock()
        except Exception as e:
            print(e)

    def activate(self):
        print("[exModule] THSensor activate")

        with self.lock:
            for _ in range(5):
                try:
                    t = self.sensor.temperature
                    h = self.sensor.humidity
                    if t is not None and h is not None:
                        self.data = [t, h]
                    break
                except RuntimeError as e:
                    print(f"DHT11 read retry: {e}")
                    time.sleep(2.5)
                except Exception as e:
                    print(f"Unexpected error: {e}")
                    time.sleep(2.5)

        self.moduleRecord.THSensor = datetime.now()

    def deactivate(self):
        pass

    def run(self):
        while True:
            self.controlFlag.THSensorEvent.wait()

            self.activate()
            (self.sensorData.temp, self.sensorData.humi) = self.data

            self.controlFlag.THSensor = False
