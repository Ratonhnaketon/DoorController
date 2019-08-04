import signal
import sys

import RPi.GPIO as GPIO

from Core.controller import StateMachine 
from States.init import init
from States.locked import locked
from States.locking import locking
from States.openDoor import openDoor
from States.unlocked import unlocked
from States.unlocking import unlocking

from KeyboardController.controller import KeyboardController
from EngineController.controller import EngineController
from DoorSensorController.controller import DoorSensorController
GPIO.setmode(GPIO.BOARD)

kbController = KeyboardController(True)
engine = EngineController(37, 38)
doorSensor = DoorSensorController(3)

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
        'isDoorOpen': doorSensor.openDoor, 
        'timeout': 10,
        'tries': 0
    },
    'init'
)

print('teste')



controller.start()

signal.pause()
