"""
Picamera2 -> CSI Port
"""

from picamera2 import Picamera2
import time

camera = Picamera2()
camera.configure(camera.create_still_configuration(main={"size": (3280, 2464)}))
camera.start()
time.sleep(2)

while True:
    key = input("\nPress any key to take picture(x: close): ")
    if key == "x":
        break
    filename = time.strftime("%y%m%d_%H%M%S") + ".jpg"
    camera.capture_file(filename)
    print(f"Saved: {filename}")

camera.stop()
