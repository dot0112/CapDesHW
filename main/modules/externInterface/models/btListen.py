from threading import Thread
from models import ControlFlag
from modules import ExModule
import bluetooth
import time
import subprocess


class BtListen(Thread):
    def __init__(self):
        Thread.__init__(self)

        self.ex = ExModule()
        self.cf = ControlFlag()

        self.modules = {
            "w": (self.ex.waterPump, "waterPump"),
            "h": (self.ex.humi, "humi"),
            "R": (self.ex.relay, "relay"),
        }

        try:
            subprocess.run(
                ["sudo", "systemctl", "restart", "bluetooth.service"], check=True
            )
            subprocess.run(["sudo", "hciconfig", "hci0", "up"], check=True)
            subprocess.run(["sudo", "hciconfig", "hci0", "piscan"], check=True)

            self.serverSock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
            self.port = 1
            self.serverSock.bind(("", self.port))
            self.serverSock.listen(1)

            self.serviceUuid = "00001101-0000-1000-8000-00805F9B34FB"

            bluetooth.advertise_service(
                self.serverSock,
                "pyum",
                service_id=self.serviceUuid,
                service_classes=[self.serviceUuid, bluetooth.SERIAL_PORT_CLASS],
                profiles=[bluetooth.SERIAL_PORT_PROFILE],
            )

        except Exception as e:
            print(e)

    def controlForce(self, module, value):
        if module in self.modules.keys():
            (moduleObj, flagField) = self.modules[module]

            if value != moduleObj.status:
                setattr(self.cf, flagField, True)

            setattr(self.cf, (flagField + "F"), True)

    def releaseForce(self):
        for _, flagField in self.modules.values():
            setattr(self.cf, (flagField + "F"), False)
        self.cf.controlForce = True

    def run(self):
        while True:
            print("BT Listen")
            try:
                clientSock, clientInfo = self.serverSock.accept()

                while True:
                    data = clientSock.recv(1024)
                    if not data:
                        print("[BT] Client disconnected")
                        break
                    print(f"[BT] Received: {data}")
                    try:
                        module, value = data.decode().strip().split(".")
                        self.controlForce(module, value == "1")
                        clientSock.send(b"ok")
                    except Exception as e:
                        print(f"BT message error: {e}")
                        clientSock.send(b"error")

                clientSock.close()
                self.releaseForce()

            except Exception as e:
                print(f"BT thread error: {e}")
                time.sleep(1)
