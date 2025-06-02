from models import singleton, SensorData
import requests
import os


@singleton
class DataUpload:
    def __init__(self):
        self.sensorData = SensorData()
        self.serverAddr = ""

    def uploadSensorData(self):
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

        response = requests.post(apiUrl, json=data)

        return response.status_code == 200

    def uploadImage(self):
        None
