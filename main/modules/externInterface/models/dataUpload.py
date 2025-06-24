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
        self.serverAddr = ""

    def getSensorData(self):
        now = datetime.now()

        self.controlFlag.camera = True
        self.controlFlag.THSensor = True
        self.controlFlag.soil = True

        while True:
            if all([
                    self.moduleRecord.camera is not None,
                    self.moduleRecord.THSensor is not None,
                    self.moduleRecord.soil is not None
                ]):
                slowest = min(self.moduleRecord.camera, self.moduleRecord.THSensor, self.moduleRecord.soil)
                print(slowest)
                if now < slowest:
                    break
                time.sleep(1)


    def uploadSensorData(self):
        result = {"sensor": None, "image": None}
        self.getSensorData()

        result ["sensor"] = self.uploadSensor()
        result ["image"] = self.uploadImage()

        return result


    def uploadSensor(self):
        apiUrl = self.serverAddr + "/api/sensor"

        data = {
            "deviceId": os.getenv("DEVICEID"),
            "temperature": self.sensorData.temp,
            "humidity": self.sensorData.humi,
            "soilTemperature": self.sensorData.soilTemp,
            "soilMoisture": self.sensorData.soilHumi,
            "soilEC": self.sensorData.soilEC,
            "soilPH": self.sensorData.soilPH,
        }
        print(f"[upload sensor]: {data}")

        try:
            response = requests.post(apiUrl, json=data)
            return response.status_code == 200
        except requests.RequestException as e:
            print(f"[upload sensor/sensor]: Request failed - {e}")
            return False

    def uploadImage(self):
        apiUrl = self.serverAddr + "/api/image"
        data = self.sensorData.cameraCapture

        success, imgEncoded = cv2.imencode('.jpg', data)
        if not success:
            print("[upload image]: Failed to encode image")
            return False

        fileBytes = imgEncoded.tobytes()

        files = {
            "image": ("leaf.jpg", fileBytes, "image/jpeg")
        }

        try:
            response = requests.post(apiUrl, files=files)
            return response.status_code == 200
        except requests.RequestException as e:
            print(f"[upload sensor/image]: Request failed - {e}")
            return False
