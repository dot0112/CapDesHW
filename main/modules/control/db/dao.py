from models import singleton
from .dbConn import dbConn
from ..models import OrchidLight, OrchidWatering, OrchidHumi


@singleton
class Dao:
    def __init__(self):
        self.conn = dbConn()
        self.cursor = self.conn.cursor()

    def getHumi(self, month):
        result = self._fetchByMonth("HUMIDIFICATION", month)
        dto = OrchidHumi()
        (dto.month, dto.minHumi, dto.maxHumi) = result
        return dto

    def getLight(self, month):
        result = self._fetchByMonth("LIGHT", month)
        dto = OrchidLight()
        (
            dto.month,
            dto.amShading,
            dto.pmShading,
        ) = result
        return dto

    def getWatering(self, month):
        result = self._fetchByMonth("WATERING", month)
        dto = OrchidWatering()
        (
            dto.month,
            dto.isDay,
            dto.interval,
        ) = result
        return dto

    def _fetchByMonth(self, tableName, month):
        allowed_tables = {"HUMIDIFICATION", "LIGHT", "WATERING"}

        if tableName not in allowed_tables:
            raise ValueError("Invalid table name")

        query = f"SELECT * FROM {tableName} WHERE MONTH = ?"

        self.cursor.execute(query, (month,))
        return self.cursor.fetchone()
