class OrchidLight:
    def __init__(self):
        self._month = 0
        self._amShading = 0
        self._pmShading = 0

    @property
    def month(self):
        return self._month

    @month.setter
    def month(self, value):
        self._month = value

    @property
    def amShading(self):
        return self._amShading

    @amShading.setter
    def amShading(self, value):
        self._amShading = value

    @property
    def pmShading(self):
        return self._pmShading

    @pmShading.setter
    def pmShading(self, value):
        self._pmShading = value
