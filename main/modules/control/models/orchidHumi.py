class OrchidHumi:
    def __init__(self):
        self._month = 0
        self._minHumi = 0
        self._maxHumi = 0

    @property
    def month(self):
        return self._month

    @month.setter
    def month(self, value):
        self._month = value

    @property
    def minHumi(self):
        return self._minHumi

    @minHumi.setter
    def minHumi(self, value):
        self._minHumi = value

    @property
    def maxHumi(self):
        return self._maxHumi

    @maxHumi.setter
    def maxHumi(self, value):
        self._maxHumi = value
