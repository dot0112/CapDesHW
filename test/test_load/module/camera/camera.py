from picamera2 import Picamera2
import time

camera = None


def actCamera(_, e):
    global camera
    if camera is None:
        camera = Picamera2()
        camera.configure(camera.create_still_configuration(main={"size": (3280, 2464)}))
        camera.start()
        time.sleep(2)

    if e == 1:
        filename = time.strftime("%y%m%d_%H%M%S") + ".jpg"
        camera.capture_file(filename)
