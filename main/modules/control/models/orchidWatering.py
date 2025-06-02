class OrchidWatering:
    def __init__(self):
        self._month = 0
        self._isDay = 0
        self._interval = 0

    @property
    def month(self):
        return self._month

    @month.setter
    def month(self, value):
        self._month = value

    @property
    def isDay(self):
        return self._isDay

    @isDay.setter
    def isDay(self, value):
        self._isDay = value

    @property
    def interval(self):
        return self._interval

    @interval.setter
    def interval(self, value):
        self._interval = value
