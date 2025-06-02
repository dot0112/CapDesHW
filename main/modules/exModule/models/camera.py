from .module import Module
from models import singleton
from picamera2 import Picamera2
from threading import Thread
from datetime import datetime
import time


@singleton
class Camera(Thread, Module):
    def __init__(self):
        Thread.__init__(self)
        self.cameraCapture = None
        self.camera = Picamera2()
        self.camera.configure(
            self.camera.create_still_configuration(main={"size": (1280, 720)})
        )
        self.camera.start()

    def activate(self):
        self.cameraCapture = self.camera.capture_array()
        self.moduleRecord.camera = datetime.now()

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
