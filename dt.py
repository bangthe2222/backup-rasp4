from gpiozero import DistanceSensor
from time import sleep
while True:
    def distance1():
        sensor = DistanceSensor(echo=24, trigger=23)
        return sensor.distance*100
    def distance2():
        sensor = DistanceSensor(echo=8, trigger=25)
        return sensor.distance*100
    print(distance1())
    print("////")
    print(distance2())
