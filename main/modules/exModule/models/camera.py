from .module import Module
from picamera2 import Picamera2
from threading import Thread
from datetime import datetime


class Camera(Thread, Module):
    def __init__(self):
        Thread.__init__(self)
        self.cameraCapture = None
        try:
            self.camera = Picamera2()
            self.camera.configure(
                self.camera.create_still_configuration(main={"size": (1280, 720)})
            )
            self.camera.start()
        except Exception as e:
            print(e)

    def activate(self):
        print("[exModule] camera activate")
        try:
            self.cameraCapture = self.camera.capture_array()
        except Exception as e:
            print(f"[error] camera error: {e}")
        self.moduleRecord.camera = datetime.now()

    def deactivate(self):
        pass

    def run(self):
        while True:
            self.controlFlag.cameraEvent.wait()

            self.activate()
            self.sensorData.cameraCapture = self.cameraCapture

            self.controlFlag.camera = False
