import threading
from models.singleton import singleton


@singleton
class ModuleRecord:
    def __init__(self):
        self._lock = threading.Lock() 
        self._camera = None
        self._waterPump = None
        self._THSensor = None
        self._humi = None
        self._relay = None
        self._soil = None

    @property
    def camera(self):
        with self._lock:
            return self._camera

    @camera.setter
    def camera(self, value):
        with self._lock:
            self._camera = value

    @property
    def waterPump(self):
        with self._lock:
            return self._waterPump

    @waterPump.setter
    def waterPump(self, value):
        with self._lock:
            self._waterPump = value

    @property
    def THSensor(self):
        with self._lock:
            return self._THSensor

    @THSensor.setter
    def THSensor(self, value):
        with self._lock:
            self._THSensor = value

    @property
    def humi(self):
        with self._lock:
            return self._humi

    @humi.setter
    def humi(self, value):
        with self._lock:
            self._humi = value

    @property
    def relay(self):
        with self._lock:
            return self._relay

    @relay.setter
    def relay(self, value):
        with self._lock:
            self._relay = value

    @property
    def soil(self):
        with self._lock:
            return self._soil

    @soil.setter
    def soil(self, value):
        with self._lock:
            self._soil = value