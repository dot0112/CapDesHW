import threading
from models.singleton import singleton


@singleton
class ModuleRecord:
    def __init__(self):
        self._lock = threading.Lock()
        self._camera = None
        self._fCamera = None
        self._waterPump = None
        self._fWaterPump = None
        self._THSensor = None
        self._fTHSensor = None
        self._humi = None
        self._fHumi = None
        self._relay = None
        self._fRelay = None
        self._soil = None
        self._fSoil = None

    @property
    def camera(self):
        with self._lock:
            return self._camera

    @camera.setter
    def camera(self, value):
        with self._lock:
            self._camera = value

    @property
    def fCamera(self):
        with self._lock:
            return self._fCamera

    @fCamera.setter
    def fCamera(self, value):
        with self._lock:
            self._fCamera = value

    @property
    def waterPump(self):
        with self._lock:
            return self._waterPump

    @waterPump.setter
    def waterPump(self, value):
        with self._lock:
            self._waterPump = value

    @property
    def fWaterPump(self):
        with self._lock:
            return self._fWaterPump

    @fWaterPump.setter
    def fWaterPump(self, value):
        with self._lock:
            self._fWaterPump = value

    @property
    def THSensor(self):
        with self._lock:
            return self._THSensor

    @THSensor.setter
    def THSensor(self, value):
        with self._lock:
            self._THSensor = value

    @property
    def fTHSensor(self):
        with self._lock:
            return self._fTHSensor

    @fTHSensor.setter
    def fTHSensor(self, value):
        with self._lock:
            self._fTHSensor = value

    @property
    def humi(self):
        with self._lock:
            return self._humi

    @humi.setter
    def humi(self, value):
        with self._lock:
            self._humi = value

    @property
    def fHumi(self):
        with self._lock:
            return self._fHumi

    @fHumi.setter
    def fHumi(self, value):
        with self._lock:
            self._fHumi = value

    @property
    def relay(self):
        with self._lock:
            return self._relay

    @relay.setter
    def relay(self, value):
        with self._lock:
            self._relay = value

    @property
    def fRelay(self):
        with self._lock:
            return self._fRelay

    @fRelay.setter
    def fRelay(self, value):
        with self._lock:
            self._fRelay = value

    @property
    def soil(self):
        with self._lock:
            return self._soil

    @soil.setter
    def soil(self, value):
        with self._lock:
            self._soil = value

    @property
    def fSoil(self):
        with self._lock:
            return self._fSoil

    @fSoil.setter
    def fSoil(self, value):
        with self._lock:
            self._fSoil = value
