import threading
from models.singleton import singleton


@singleton
class SensorData:
    def __init__(self):
        self._lock = threading.Lock()
        self._cameraCapture = None
        self._temp = 0.0
        self._humi = 0.0
        self._soilTemp = 0.0
        self._soilHumi = 0.0
        self._soilEC = 0.0
        self._soilPH = 0.0

    @property
    def cameraCapture(self):
        with self._lock:
            return self._cameraCapture

    @cameraCapture.setter
    def cameraCapture(self, value):
        with self._lock:
            self._cameraCapture = value

    @property
    def temp(self):
        with self._lock:
            return self._temp

    @temp.setter
    def temp(self, value):
        with self._lock:
            self._temp = value

    @property
    def humi(self):
        with self._lock:
            return self._humi

    @humi.setter
    def humi(self, value):
        with self._lock:
            self._humi = value

    @property
    def soilTemp(self):
        with self._lock:
            return self._soilTemp

    @soilTemp.setter
    def soilTemp(self, value):
        with self._lock:
            self._soilTemp = value

    @property
    def soilHumi(self):
        with self._lock:
            return self._soilHumi

    @soilHumi.setter
    def soilHumi(self, value):
        with self._lock:
            self._soilHumi = value

    @property
    def soilEC(self):
        with self._lock:
            return self._soilEC

    @soilEC.setter
    def soilEC(self, value):
        with self._lock:
            self._soilEC = value

    @property
    def soilPH(self):
        with self._lock:
            return self._soilPH

    @soilPH.setter
    def soilPH(self, value):
        with self._lock:
            self._soilPH = value
