from singleton import singleton


@singleton
class ModuleRecord:
    def __init__(self):
        self._camera = None
        self._waterPump = None
        self._THSensor = None
        self._humi = None
        self._relay = None
        self._soil = None

    @property
    def camera(self):
        return self._camera

    @camera.setter
    def camera(self, value):
        self._camera = value

    @property
    def waterPump(self):
        return self._waterPump

    @waterPump.setter
    def waterPump(self, value):
        self._waterPump = value

    @property
    def THSensor(self):
        return self._THSensor

    @THSensor.setter
    def THSensor(self, value):
        self._THSensor = value

    @property
    def humi(self):
        return self._humi

    @humi.setter
    def humi(self, value):
        self._humi = value

    @property
    def relay(self):
        return self._relay

    @relay.setter
    def relay(self, value):
        self._relay = value

    @property
    def soil(self):
        return self._soil

    @soil.setter
    def soil(self, value):
        self._soil = value
