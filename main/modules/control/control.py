from models import SensorData, ControlFlag, ModuleRecord, singleton
from .db import Dao
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler


@singleton
class Control:
    def __init__(self):
        self.scheduler = BackgroundScheduler()
        self.sensorData = SensorData()
        self.controlFlag = ControlFlag()
        self.moduleRecord = ModuleRecord()

        self.dao = Dao()

        """
        spring: 춘란
        summer: 하란
        authum: 추란
        winter: 한란
        """
        self.category = "spring"
        self.month = datetime.now().month

        self.wateringInterval = 0

        self.scheduler.start()

    def setOrchidCategory(self, category):
        allowedCategory = ["spring", "summer", "authum", "winter"]

        if category not in allowedCategory:
            raise ValueError("Invalid category")

        self.category = category

    def _updateMonth(self):
        self.month = datetime.now().month

    def setWateringStatus(self):
        self._updateMonth()
        dto = self.dao.getWatering()
        self.wateringInterval = max(dto.interval)

        sensorData = self.sensorData.soilHumi
        latestWatering = self.moduleRecord.waterPump

        dayDiff = (datetime.now() - latestWatering).days

        return (
            (sensorData < 30) and (dayDiff >= self.wateringInterval),
            dto.isDay,
        )  # needWatering, isDay

    def setTempStatus(self, isDay):
        self._updateMonth()
        dto = self.dao.getTemp()
        sensorData = self.sensorData.temp

        if isDay:
            minT, avgT, maxT = dto.dayMinTemp, dto.dayAvgTemp, dto.dayMaxTemp
        else:
            minT, avgT, maxT = dto.nightMinTemp, dto.nightAvgTemp, dto.nightMaxTemp

        if sensorData < minT:
            diff = sensorData - minT
        elif sensorData > maxT:
            diff = sensorData - maxT
        else:
            diff = 0

        return (diff, avgT)

    def setHumiStatus(self):
        self._updateMonth()
        dto = self.dao.getHumi()
        sensorData = self.sensorData.humi

        if sensorData < dto.minHumi:
            diff = sensorData - dto.minHumi
        elif sensorData > dto.maxHumi:
            diff = sensorData - dto.maxHumi
        else:
            diff = 0

        return (diff, dto.avgHumi)  # diff, avg

    def setLightingStatus(self):
        self._updateMonth()
        dto = self.dao.getLight()

        return 7 + (12 * (dto.pmShading / 100))  # end time

    def setControl(self):
        None
