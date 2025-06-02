from abc import *
from models import SensorData, ControlFlag, ModuleRecord


class Module(metaclass=ABCMeta):
    sensorData = SensorData()
    controlFlag = ControlFlag()
    moduleRecord = ModuleRecord()

    @abstractmethod
    def activate(self):
        pass

    @abstractmethod
    def deactivate(self):
        pass
