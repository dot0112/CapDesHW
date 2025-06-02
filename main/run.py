from models import SensorData, ControlFlag, ModuleRecord
from modules import ExModule, Control, ExternInterface
import RPi.GPIO as g
import time


def main():
    g.setmode(g.BCM)
    SensorData()
    ControlFlag()
    ModuleRecord()

    print("Init")

    moduleControl = ExModule()
    moduleControl.runAll()
    print("Module Run Complete")

    externInterface = ExternInterface()
    externInterface.start()
    print("Extern Interface Run Complete")

    while True:
        time.sleep(1)


if __name__ == "__main__":
    main()
