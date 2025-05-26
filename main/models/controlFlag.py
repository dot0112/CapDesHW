import threading
from singleton import singleton


@singleton
class ControlFlag:
    def __init__(self):
        self._lock = threading.Lock()
        self._camera = False
        self._THSensor = False
        self._relay = False
        self._waterPump = False
        self._humi = False
        self._soil = False

    @property
    def camera(self):
        with self._lock:
            return self._camera

    @camera.setter
    def camera(self, value):
        with self._lock:
            self._camera = bool(value)

    @property
    def THSensor(self):
        with self._lock:
            return self._THSensor

    @THSensor.setter
    def THSensor(self, value):
        with self._lock:
            self._THSensor = bool(value)

    @property
    def relay(self):
        with self._lock:
            return self._relay

    @relay.setter
    def relay(self, value):
        with self._lock:
            self._relay = bool(value)

    @property
    def waterPump(self):
        with self._lock:
            return self._waterPump

    @waterPump.setter
    def waterPump(self, value):
        with self._lock:
            self._waterPump = bool(value)

    @property
    def humi(self):
        with self._lock:
            return self._humi

    @humi.setter
    def humi(self, value):
        with self._lock:
            self._humi = bool(value)

    @property
    def soil(self):
        with self._lock:
            return self._soil

    @soil.setter
    def soil(self, value):
        with self._lock:
            self._soil = bool(value)
