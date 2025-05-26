from singleton import singleton


@singleton
class ControlFlag:
    def __init__(self):
        self._camera = False
        self._THSensor = False
        self._relay = False
        self._waterPump = False
        self._humi = False
        self._soil = False

    @property
    def camera(self):
        return self._camera

    @camera.setter
    def camera(self, value):
        self._camera = bool(value)

    @property
    def THSensor(self):
        return self._THSensor

    @THSensor.setter
    def THSensor(self, value):
        self._THSensor = bool(value)

    @property
    def relay(self):
        return self._relay

    @relay.setter
    def relay(self, value):
        self._relay = bool(value)

    @property
    def waterPump(self):
        return self._waterPump

    @waterPump.setter
    def waterPump(self, value):
        self._waterPump = bool(value)

    @property
    def humi(self):
        return self._humi

    @humi.setter
    def humi(self, value):
        self._humi = bool(value)

    @property
    def soil(self):
        return self._soil

    @soil.setter
    def soil(self, value):
        self._soil = bool(value)
