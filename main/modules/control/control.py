from models import SensorData, ControlFlag, ModuleRecord, singleton
from .db import Dao
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from modules import ExModule
import time
import threading
import math
from threading import Thread


@singleton
class Control(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.scheduler = BackgroundScheduler()
        self.sensorData = SensorData()
        self.controlFlag = ControlFlag()
        self.moduleRecord = ModuleRecord()
        self.ex = ExModule()

        self.dao = Dao()

        self.month = datetime.now().month

        self.wateringInterval = 0

        self.schedule = {"W": 0, "startL": 0, "endL": 0, "minH": 0, "maxH": 0}

        self.scheduler.add_job(
            self.setTodaySchedule,
            trigger="cron",
            hour=0,
            minute=0,
            name="dailyScheduleSetting",
        )
        self.setTodaySchedule()

        self.scheduler.start()

    def setTodaySchedule(self):
        self.month = datetime.now().month
        self.schedule = {"W": 0, "startL": 0, "endL": 0}

        for job_id in ["watering", "startLighting", "endLighting", "humidification"]:
            try:
                self.scheduler.remove_job(job_id)
            except:
                pass

        wateringSchedule = self.getWateringSchedule()
        if wateringSchedule["needWatering"]:
            self.schedule["W"] = 8 if wateringSchedule["isDay"] else 17
            self.scheduler.add_job(
                self.watering,
                trigger="cron",
                hour=self.schedule["W"],
                minute=0,
                name="watering",
            )

        (self.schedule["startL"], self.schedule["endL"]) = self.getLightingSchedule()
        (self.schedule["minH"], self.schedule["maxH"]) = self.getHumiSchedule()

        self.scheduler.add_job(
            self.lighting,
            trigger="cron",
            hour=self.schedule["startL"],
            minute=0,
            name="startLighting",
        )  # 전등 시작
        self.scheduler.add_job(
            self.lighting,
            trigger="cron",
            hour=self.schedule["endL"],
            minute=0,
            name="endLighting",
        )  # 전등 종료
        self.scheduler.add_job(
            self.humidification, trigger="interval", minutes=5, name="humidification"
        )

    def getWateringSchedule(self):
        dto = self.dao.getWatering(self.month)

        self.wateringInterval = max(dto.interval, self.wateringInterval)
        lastWatering = self.moduleRecord.waterPump

        dayDiff = 999 if lastWatering is None else (datetime.now() - lastWatering).days

        needWatering = dayDiff >= self.wateringInterval

        return {"needWatering": needWatering, "isDay": dto.isDay}

    def getLightingSchedule(self):

        dto = self.dao.getLight(self.month)
        return (
            7 + math.floor((5 * (dto.amShading) / 100)),
            13 + math.ceil((5 * ((100 - dto.pmShading) / 100))),
        )

    def getHumiSchedule(self):
        dto = self.dao.getHumi(self.month)
        return (dto.minHumi, dto.maxHumi)

    def watering(self):
        print("[watering]")
        if not self.controlFlag.waterPumpF:
            if self.schedule["W"] != 0:
                nowHour = datetime.now().hour
                if nowHour in (self.schedule["W"], self.schedule["W"] + 1):
                    self.controlFlag.waterPump = True
                    while True:
                        print(f"[control:watering] soilHumiData: {soilHumiData}")
                        self.controlFlag.soil = True
                        time.sleep(0.1)
                        soilHumiData = self.sensorData.soilHumi
                        if self.controlFlag.waterPumpF or self.controlFlag.setF:
                            print("[control:watering] break by force watering")
                            self.controlFlag.waterPump = True
                            break
                        if soilHumiData is not None and soilHumiData >= 45:
                            self.controlFlag.waterPump = True
                            break
                else:
                    if self.ex.waterPump.status == True:
                        self.controlFlag.waterPump = True

    def lighting(self):
        print("[lighting]")
        if not self.controlFlag.relayF:
            nowHour = datetime.now().hour
            if self.schedule["startL"] <= nowHour < self.schedule["endL"]:
                if not self.ex.relay.status:
                    self.controlFlag.relay = True
            else:
                if self.ex.relay.status:
                    self.controlFlag.relay = True

    def humidification(self):
        if not self.controlFlag.humiF:
            self.controlFlag.THSensor = True
            time.sleep(2.5)
            humiData = self.sensorData.humi

            if humiData < self.schedule["minH"]:
                self.controlFlag.humi = True
                while True:
                    print(1)
                    self.controlFlag.THSensor = True
                    humiData = self.sensorData.humi
                    time.sleep(2.5)
                    print(f"[control:humidification] humiData: {humiData}")
                    if self.controlFlag.humiF or self.controlFlag.setF:
                        print("[control:humi] break by force humi")
                        self.controlFlag.humi = True
                        break
                    if humiData >= self.schedule["maxH"]:
                        print(
                            f"[control:humi] over maxH: {humiData}/{self.schedule['maxH']}"
                        )
                        self.controlFlag.humi = True
                        break

    def runThread(self):
        threads = [
            threading.Thread(target=self.watering),
            threading.Thread(target=self.lighting),
            threading.Thread(target=self.humidification),
        ]

        for t in threads:
            t.start()

        for t in threads:
            t.join()

    def setReleaseControl(self):
        self.controlFlag.releaseFEvent.wait()

        self.runThread()

        self.controlFlag.releaseF = False

    def run(self):
        self.setTodaySchedule()
        self.runThread()
        while True:
            self.setReleaseControl()
