from .module import Module
from main.models import singleton
from picamera2 import Picamera2


@singleton
class camera(Module):
    def __init__(self):
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
