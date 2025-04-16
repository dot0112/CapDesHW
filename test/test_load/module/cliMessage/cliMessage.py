import os
import camera
import temHum
import relay
import waterPump
import humidification
import soilSensor


messageBuf = """
Camera:\t\t\t (%d)
Temperature/Humidity: \t (%d) %10.2f *C%10.2f %%
Relay: \t\t\t (%d)
WaterPump: \t\t (%d)
Humidification: \t (%d)
SoilSensor: \t\t (%d) %10.2f *C%10.2f %%%10.2f us/cm%10.2f ph

(0: Camera, 1: temHum, 2: relay, 3: waterPump, 4: humi, 5: soil): 
"""


def printCliMessage(eventList=[0, 0, 0, 0, 0, 0]):
    os.system("clear")
    temp, humi, soilTemp, soilHumi, soilEC, soilPH = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0
    message = messageBuf % (
        eventList[0],
        eventList[1],
        temp,
        humi,
        eventList[2],
        eventList[3],
        eventList[4],
        eventList[5],
        soilTemp,
        soilHumi,
        soilEC,
        soilPH,
    )

    print(message, end="")
