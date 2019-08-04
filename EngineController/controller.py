# import RPi.GPIO as GPIO

class EngineController:
    def __init__(self):
        self.rotation = 0
        self.working = 0

    def assignPins(self, pin_in1, pin_in2):
        self.pin_in1 = pin_in1
        self.pin_in2 = pin_in2
        GPIO.setup(pin_in1, GPIO.OUT)
        GPIO.setup(pin_in2, GPIO.OUT)
        self.stop()

    def rotateClockWise(self):
        GPIO.output(self.pin_in1, GPIO.HIGH)
        GPIO.output(self.pin_in2, GPIO.LOW)

    def stop(self):
        GPIO.output(self.pin_in1, GPIO.LOW)
        GPIO.output(self.pin_in2, GPIO.LOW)

    def rotateCounterClockWise(self):
        GPIO.output(self.pin_in1, GPIO.LOW)
        GPIO.output(self.pin_in2, GPIO.HIGH)

engine = EngineController()
