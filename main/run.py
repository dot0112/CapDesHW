from models import SensorData, ControlFlag, ModuleRecord
import RPi.GPIO as g


def main():
    g.setmode(g.BCM)
    SensorData()
    ControlFlag()
    ModuleRecord()


if __name__ == "__main__":
    main()
