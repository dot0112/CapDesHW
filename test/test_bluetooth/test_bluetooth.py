import bluetooth
import subprocess


def restart_bluetooth_service():
    subprocess.run(["sudo", "systemctl", "restart", "bluetooth.service"], check=True)


def setup_bluetooth_interface():
    subprocess.run(["sudo", "hciconfig", "hci0", "up"], check=True)
    subprocess.run(["sudo", "hciconfig", "hci0", "piscan"], check=True)


restart_bluetooth_service()
setup_bluetooth_interface()


server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
port = 3
server_sock.bind(("", port))
server_sock.listen(1)

service_uuid = "00001101-0000-1000-8000-00805F9B34FB"

print([bluetooth.SERIAL_PORT_CLASS])
print([bluetooth.SERIAL_PORT_PROFILE])

bluetooth.advertise_service(
    server_sock,
    "pyum",
    service_id=service_uuid,
    service_classes=[service_uuid, bluetooth.SERIAL_PORT_CLASS],
    profiles=[bluetooth.SERIAL_PORT_PROFILE],
)

print(f"Waiting for connection on RFCOMM channel {port}")

client_sock, client_info = server_sock.accept()
print("Accepted connection from ", client_info)

data = client_sock.recv(1024)
print("Received: ", data)

client_sock.close()
server_sock.close()
