from .module import Module
from main.models import singleton
from picamera2 import Picamera2
from threading import Thread
import time


@singleton
class camera(Thread, Module):
    def __init__(self):
        Thread.__init__(self)
        self.cameraCapture = None
        self.camera = Picamera2()
        self.camera.configure(
            self.camera.create_still_configuration(main={"size": (3280, 2464)})
        )
        self.camera.start()

    def activate(self):
        self.cameraCapture = self.camera.capture_image("main")

    def deactivate(self):
        pass

    def run(self):
        while True:
            with self.controlFlag._lock:
                if self.controlFlag.camera:
                    self.activate()
                    self.sensorData.cameraCapture = self.cameraCapture
                    self.controlFlag.camera = False
                time.sleep(1)
