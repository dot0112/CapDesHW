from models import singleton
from .models import Camera, Humi, Relay, Soil, THSensor, WaterPump


@singleton
class ExModule:
    def __init__(self):
        self._camera = Camera()
        self._humi = Humi()
        self._relay = Relay()
        self._soil = Soil()
        self._THSensor = THSensor()
        self._waterPump = WaterPump()

    def runAll(self):
        print("camera run")
        self._camera.start()
        print("humi run")
        self._humi.start()
        print("relay run")
        self._relay.start()
        print("soil run")
        self._soil.start()
        print("thsensor run")
        self._THSensor.start()
        print("waterpump run")
        self._waterPump.start()

    @property
    def camera(self):
        return self._camera

    @property
    def humi(self):
        return self._humi

    @property
    def relay(self):
        return self._relay

    @property
    def soil(self):
        return self._soil

    @property
    def THSensor(self):
        return self._THSensor

    @property
    def waterPump(self):
        return self._waterPump
