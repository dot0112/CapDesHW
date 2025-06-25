from threading import Event, RLock
from models.singleton import singleton


@singleton
class ControlFlag:
    def __init__(self):
        self._camera = Event()
        self._THSensor = Event()
        self._relay = Event()
        self._waterPump = Event()
        self._humi = Event()
        self._soil = Event()

        self._setF = Event()
        self._releaseF = Event()
        self._relayF = False
        self._waterPumpF = False
        self._humiF = False

    @property
    def camera(self):
        return self._camera.is_set()

    @camera.setter
    def camera(self, value):
        if value:
            self._camera.set()
        else:
            self._camera.clear()

    @property
    def THSensor(self):
        return self._THSensor.is_set()

    @THSensor.setter
    def THSensor(self, value):
        if value:
            self._THSensor.set()
        else:
            self._THSensor.clear()

    @property
    def relay(self):
        return self._relay.is_set()

    @relay.setter
    def relay(self, value):
        if value:
            self._relay.set()
        else:
            self._relay.clear()

    @property
    def waterPump(self):
        return self._waterPump.is_set()

    @waterPump.setter
    def waterPump(self, value):
        if value:
            self._waterPump.set()
        else:
            self._waterPump.clear()

    @property
    def humi(self):
        return self._humi.is_set()

    @humi.setter
    def humi(self, value):
        if value:
            self._humi.set()
        else:
            self._humi.clear()

    @property
    def soil(self):
        return self._soil.is_set()

    @soil.setter
    def soil(self, value):
        if value:
            self._soil.set()
        else:
            self._soil.clear()

    @property
    def releaseF(self):
        return self._releaseF.is_set()

    @releaseF.setter
    def releaseF(self, value):
        if value:
            self._releaseF.set()
        else:
            self._releaseF.clear()

    @property
    def setF(self):
        return self._setF.is_set()

    @setF.setter
    def setF(self, value):
        if value:
            self._setF.set()
        else:
            self._setF.clear()

    @property
    def waterPumpF(self):
        return self._waterPumpF

    @waterPumpF.setter
    def waterPumpF(self, value):
        self._waterPumpF = value

    @property
    def humiF(self):
        return self._humiF

    @humiF.setter
    def humiF(self, value):
        self._humiF = value

    @property
    def relayF(self):
        return self._relayF

    @relayF.setter
    def relayF(self, value):
        self._relayF = value

    @property
    def cameraEvent(self):
        return self._camera

    @property
    def THSensorEvent(self):
        return self._THSensor

    @property
    def relayEvent(self):
        return self._relay

    @property
    def waterPumpEvent(self):
        return self._waterPump

    @property
    def humiEvent(self):
        return self._humi

    @property
    def soilEvent(self):
        return self._soil

    @property
    def releaseFEvent(self):
        return self._releaseF
