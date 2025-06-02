class OrchidTemp:
    def __init__(self):
        self._month = 0
        self._dayMinTemp = 0
        self._dayAvgTemp = 0
        self._dayMaxTemp = 0
        self._nightMinTemp = 0
        self._nightAvgTemp = 0
        self._nightMaxTemp = 0

    @property
    def month(self):
        return self._month

    @month.setter
    def month(self, value):
        self._month = value

    @property
    def dayMinTemp(self):
        return self._dayMinTemp

    @dayMinTemp.setter
    def dayMinTemp(self, value):
        self._dayMinTemp = value

    @property
    def dayAvgTemp(self):
        return self._dayAvgTemp

    @dayAvgTemp.setter
    def dayAvgTemp(self, value):
        self._dayAvgTemp = value

    @property
    def dayMaxTemp(self):
        return self._dayMaxTemp

    @dayMaxTemp.setter
    def dayMaxTemp(self, value):
        self._dayMaxTemp = value

    @property
    def nightMinTemp(self):
        return self._nightMinTemp

    @nightMinTemp.setter
    def nightMinTemp(self, value):
        self._nightMinTemp = value

    @property
    def nightAvgTemp(self):
        return self._nightAvgTemp

    @nightAvgTemp.setter
    def nightAvgTemp(self, value):
        self._nightAvgTemp = value

    @property
    def nightMaxTemp(self):
        return self._nightMaxTemp

    @nightMaxTemp.setter
    def nightMaxTemp(self, value):
        self._nightMaxTemp = value
