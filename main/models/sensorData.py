from singleton import singleton


@singleton
class SensorData:
    def __init__(self):
        self._cameraCapture = None
        self._temp = 0.0
        self._humi = 0.0
        self._soilTemp = 0.0
        self._soilHumi = 0.0
        self._soilEC = 0.0
        self._soilPH = 0.0

    @property
    def cameraCapture(self):
        return self._cameraCapture

    @cameraCapture.setter
    def cameraCapture(self, value):
        self._cameraCapture = value

    @property
    def temp(self):
        return self._temp

    @temp.setter
    def temp(self, value):
        self._temp = value

    @property
    def humi(self):
        return self._humi

    @humi.setter
    def humi(self, value):
        self._humi = value

    @property
    def soilTemp(self):
        return self._soilTemp

    @soilTemp.setter
    def soilTemp(self, value):
        self._soilTemp = value

    @property
    def soilHumi(self):
        return self._soilHumi

    @soilHumi.setter
    def soilHumi(self, value):
        self._soilHumi = value

    @property
    def soilEC(self):
        return self._soilEC

    @soilEC.setter
    def soilEC(self, value):
        self._soilEC = value

    @property
    def soilPH(self):
        return self._soilPH

    @soilPH.setter
    def soilPH(self, value):
        self._soilPH = value
