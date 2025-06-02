from .models import Camera, Humi, Relay, Soil, THSensor, WaterPump


class ExModule:
    def __init__(self):
        self.camera = Camera()
        self.humi = Humi()
        self.relay = Relay()
        self.soil = Soil()
        self.THSensor = THSensor()
        self.waterPump = WaterPump()

    def runAll(self):
        print("camera run")
        self.camera.start()
        print("humi run")
        self.humi.start()
        print("relay run")
        self.relay.start()
        print("soil run")
        self.soil.start()
        print("thsensor run")
        self.THSensor.start()
        print("waterpump run")
        self.waterPump.start()
