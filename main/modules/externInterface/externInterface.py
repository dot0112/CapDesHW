from models import singleton
from threading import Thread
from .modules import ConnectWiFi, DataUpload, RequestCallback
from apscheduler.schedulers.background import BackgroundScheduler
import time


@singleton
class ExternInterface(Thread):
    def __init__(self):
        Thread.__init__(self)

        self.connectWiFi = ConnectWiFi()
        self.dataUpload = DataUpload()
        self.requestCallback = RequestCallback()
        self.scheduler = BackgroundScheduler()

        if self.connectWiFi.loadData() == 0:
            self.connectWiFi.connect()

        self.scheduler.add_job(func=self.uploadSensor, trigger="interval", minutes=5)
        self.scheduler.start()

    def run(self):
        while True:
            try:
                if self.connectWiFi.status() is None:
                    qr = self.connectWiFi.qrScan()
                    if qr and self.connectWiFi.parseWifiQr():
                        self.connectWiFi.connect()
            except Exception as e:
                print(f"WiFi thread error: {e}")
            time.sleep(1)

    def uploadSensor(self):
        try:
            result = self.dataUpload.uploadSensorData()
        except Exception as e:
            print(f"[ERROR] Upload Error: {e}")
