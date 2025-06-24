from models import singleton
from .modules import ConnectWiFi, DataUpload, RequestCallback, BtListen
from apscheduler.schedulers.background import BackgroundScheduler
import time


@singleton
class ExternInterface:
    def __init__(self):

        self.connectWiFi = ConnectWiFi()
        self.dataUpload = DataUpload()
        self.requestCallback = RequestCallback()
        self.btListen = BtListen()
        self.scheduler = BackgroundScheduler()

        if self.connectWiFi.loadData() == 0:
            self.connectWiFi.connect()

        self.scheduler.add_job(func=self.uploadSensor, trigger="cron", minute="*/1")
        self.scheduler.start()

    def runAll(self):
        print("connectWiFi run")
        self.connectWiFi.start()
        print("btListen run")
        self.btListen.start()

    def uploadSensor(self):
        if self.connectWiFi.status() is not None:
            try:
                print(f"[INFO] Upload started at {time.strftime('%Y-%m-%d %H:%M:%S')}")
                result = self.dataUpload.uploadSensorData()
            except Exception as e:
                print(f"[ERROR] Upload Error: {e}")
