from models import SensorData, ControlFlag, ModuleRecord
from modules import ExModule, Control, ExternInterface
import RPi.GPIO as g
import time


def main():
    try:
        g.setmode(g.BCM)
        SensorData()
        ControlFlag()
        ModuleRecord()

        print("Init")

        exModule = ExModule()
        exModule.runAll()
        print("Module Run Complete")

        control = Control()
        control.start()
        print("Control Run Complete")

        externInterface = ExternInterface()
        externInterface.runAll()
        print("Extern Interface Run Complete")

        while True:
            time.sleep(1)
    finally:
        exModule.clear()


if __name__ == "__main__":
    main()
