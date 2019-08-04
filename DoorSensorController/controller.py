import RPi.GPIO as GPIO
from threading import Thread

class DoorSensorController(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.doorIsOpen = False
        self.daemon = True

    def assignPin(self, pin):
        self.pin = pin
        GPIO.setup(pin, GPIO.IN)

    def run(self):
        while (1):
            self.doorIsOpen = GPIO.input(self.pin) == GPIO.LOW
doorSensor = DoorSensorController()