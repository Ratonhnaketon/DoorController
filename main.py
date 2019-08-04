import signal
import sys

import RPi.GPIO as GPIO

from ServerController.controller import svrController

from Core.controller import StateMachine 
from States.init import init
from States.locked import locked
from States.locking import locking
from States.openDoor import openDoor
from States.unlocked import unlocked
from States.unlocking import unlocking

from KeyboardController.controller import kbController
from EngineController.controller import engine
from DoorSensorController.controller import doorSensor

GPIO.setmode(GPIO.BOARD)

engine.assignPins(37, 38)
doorSensor.assignPin(3)

kbController.start()
doorSensor.start()


controller = StateMachine(
    { 
        'init': init, 
        'locked': locked,
        'unlocking': unlocking, 
        'unlocked': unlocked, 
        'openDoor': openDoor, 
        'locking': locking
    },
    { 
        'requesting': False, 
        'isDoorOpen': doorSensor.doorIsOpen, 
        'timeout': 10,
        'tries': 0
    },
    'init'
)


# kbController.start()
controller.start()
svrController.config(5000, False, False)
svrController.start()
# kbController.join()
