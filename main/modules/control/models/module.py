from abc import *
from main.models import SensorData, ControlFlag


class Module(metaclass=ABCMeta):
    sensorData = SensorData()
    controlFlag = ControlFlag()

    @abstractmethod
    def activate(self):
        pass

    @abstractmethod
    def deactivate(self):
        pass
