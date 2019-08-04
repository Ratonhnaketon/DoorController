import RPi.GPIO as GPIO
from threading import Thread

class DoorSensorController(Thread):
    def __init__(self, pin):
        self.doorOpen = False
        self.pin = pin
        GPIO.setup(pin, GPIO.IN)

    def run(self):
        while (1):
            self.doorOpen = GPIO.input(self.pin) == GPIO.LOW