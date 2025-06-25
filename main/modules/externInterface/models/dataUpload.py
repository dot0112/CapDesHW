from models import SensorData, ControlFlag, ModuleRecord
from datetime import datetime
import cv2
import requests
import os
import time


class DataUpload:
    def __init__(self):
        self.sensorData = SensorData()
        self.controlFlag = ControlFlag()
        self.moduleRecord = ModuleRecord()
        self.serverAddr = "http://134.185.115.80:8080"

    def getSensorData(self):
        now = datetime.now()

        self.controlFlag.camera = True
        self.controlFlag.THSensor = True
        self.controlFlag.soil = True

        while True:
            if all(
                [
                    self.moduleRecord.camera is not None,
                    self.moduleRecord.THSensor is not None,
                    self.moduleRecord.soil is not None,
                ]
            ):
                slowest = min(
                    self.moduleRecord.camera,
                    self.moduleRecord.THSensor,
                    self.moduleRecord.soil,
                )
                print(slowest)
                if now < slowest:
                    break
                time.sleep(1)

    def uploadSensorData(self):
        result = {"sensor": None, "image": None}
        self.getSensorData()

        result["sensor"] = self.uploadSensor()
        result["image"] = self.uploadImage()

        return result

    def uploadSensor(self):
        print("uploadSensor")
        apiUrl = self.serverAddr + "/api/sensor"

        data = {
            "deviceId": os.getenv("DEVICEID"),
            "temperature": round(self.sensorData.temp, 2),  # 1 자리
            "humidity": round(self.sensorData.humi, 2),
            "soilTemperature": round(self.sensorData.soilTemp, 2),
            "soilMoisture": round(self.sensorData.soilHumi, 2),
            "soilEC": round(self.sensorData.soilEC, 2),  # 2 자리
            "soilPH": round(self.sensorData.soilPH, 2),  # 2 자리
        }
        print(f"[upload sensor]: {data}")

        try:
            response = requests.post(apiUrl, json=data)
            return response.status_code == 200
        except requests.RequestException as e:
            print(f"[upload sensor/sensor]: Request failed - {e}")
            return False

    def uploadImage(self):
        print("uploadImage")
        apiUrl = self.serverAddr + "/api/image/upload"
        data = self.sensorData.cameraCapture

        success, imgEncoded = cv2.imencode(".jpg", data)
        if not success:
            print("[upload image]: Failed to encode image")
            return False

        fileBytes = imgEncoded.tobytes()

        files = {"file": ("leaf.jpg", fileBytes, "image/jpeg")}

        try:
            response = requests.post(apiUrl, files=files)
            return response.status_code == 200
        except requests.RequestException as e:
            print(f"[upload sensor/image]: Request failed - {e}")
            return False
