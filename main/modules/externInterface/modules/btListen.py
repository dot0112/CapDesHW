from threading import Thread
import bluetooth
import time
import subprocess


class BtListen(Thread):
    def __init__(self):
        Thread.__init__(self)

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

                clientSock.close()

            except Exception as e:
                print(f"BT thread error: {e}")
                time.sleep(1)
