import os
import time
from .. import camera
from .. import temHum
from .. import relay
from .. import waterPump
from .. import humidification
from .. import soilSensor


eventFuncList = [
    camera.actCamera,
    temHum.actTemHum,
    relay.actRelay,
    waterPump.actWaterPump,
    humidification.actHumidification,
    soilSensor.actSoilSensor,
]

messageBuf = """
----- Load Test -----
Current Time: %s

Camera:\t\t\t (%d)
Temperature/Humidity: \t (%d) %10.2f *C%10.2f %%
Relay: \t\t\t (%d)
WaterPump: \t\t (%d)
Humidification: \t (%d)
SoilSensor: \t\t (%d) %10.2f *C%10.2f %%%10.2f us/cm%10.2f ph

(0: Camera, 1: temHum, 2: relay, 3: waterPump, 4: humi, 5: soil): 
"""


def printCliMessage(eventList=[0, 0, 0, 0, 0, 0]):

    dataBuf = {
        "temp": 0.0,
        "humi": 0.0,
        "soilTemp": 0.0,
        "soilHumi": 0.0,
        "soilEC": 0.0,
        "soilPH": 0.0,
    }

    for idx, e in enumerate(eventList):
        eventFuncList[idx](dataBuf, e)

    message = messageBuf % (
        time.strftime("%y/%m/%d %H:%M:%S"),
        eventList[0],
        eventList[1],
        dataBuf["temp"],
        dataBuf["humi"],
        eventList[2],
        eventList[3],
        eventList[4],
        eventList[5],
        dataBuf["soilTemp"],
        dataBuf["soilHumi"],
        dataBuf["soilEC"],
        dataBuf["soilPH"],
    )
    os.system("clear")
    print(message, end="")
