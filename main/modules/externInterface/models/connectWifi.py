from models import ControlFlag, SensorData
from threading import Thread
from pyzbar.pyzbar import decode
import subprocess
import time
import re


class ConnectWiFi(Thread):
    def __init__(self):
        Thread.__init__(self)

        self.SSID = ""
        self.PW = ""
        self.image = None
        self.rawData = ""

        self.controlFlag = ControlFlag()
        self.sensorData = SensorData()

    def status(self):
        try:
            ssid = subprocess.check_output(["iwgetid", "-r"]).decode().strip()
            return ssid if ssid else None
        except subprocess.CalledProcessError:
            return None

    def saveData(self):
        with open("wifi.txt", "w", encoding="utf-8") as f:
            f.write(f"{self.SSID}/{self.PW}")

    def loadData(self):
        try:
            data = None
            with open("wifi.txt", "r", encoding="utf-8") as f:
                data = f.readline()

            (self.SSID, self.PW) = data.strip().split("/")
            return 0
        except Exception as e:
            return 1

    def qrScan(self, timeOut=10):
        captureStart = time.time()

        while True:
            self.controlFlag.camera = True
            newImage = self.sensorData.cameraCapture

            if newImage is not None and id(newImage) != id(self.image):
                self.image = newImage

                decodedObjects = decode(self.image)
                if decodedObjects:
                    qrData = decodedObjects[0].data.decode("utf-8")
                    self.rawData = qrData
                    return qrData

            if (time.time() - captureStart) > timeOut:
                return None

            time.sleep(0.05)

    def parseWifiQr(self):
        qrRegex = r"WIFI:S:(.*?);T:(.*?);P:(.*?);(?:H:(.*?);)?;"
        match = re.search(qrRegex, self.rawData)
        if match:
            ssid, encryption, password, hidden = match.groups()
            self.SSID = ssid
            self.PW = password
            return (ssid, password)
        else:
            return None

    def disconnect(self):
        result = subprocess.run(
            ["nmcli", "-t", "-f", "DEVICE,TYPE", "device", "status"],
            capture_output=True,
            text=True,
        )
        for line in result.stdout.strip().split("\n"):
            dev, dtype = line.split(":")
            if dtype == "wifi":
                subprocess.run(["sudo", "nmcli", "device", "disconnect", dev])
        return True

    def connect(self):
        if not self.SSID or not self.PW:
            if self.loadData() != 0:
                return False
        result = subprocess.run(
            [
                "sudo",
                "nmcli",
                "device",
                "wifi",
                "connect",
                self.SSID,
                "password",
                self.PW,
            ]
        )
        if result.returncode == 0:
            self.saveData()
        return result.returncode == 0

    def run(self):
        try:
            while True:
                if self.status() is None:
                    qr = self.qrScan()
                    if qr and self.parseWifiQr():
                        self.connect()
                else:
                    time.sleep(5)
                time.sleep(1)
        except Exception as e:
            print(f"WiFi thread error: {e}")
            time.sleep(5)
