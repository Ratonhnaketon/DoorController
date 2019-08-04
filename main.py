from Core.controller import StateMachine 

from States.init import init
from States.locking import locking
from States.openDoor import openDoor
from States.unlocked import unlocked
from States.unlocking import unlocking

from KeyboardController.controller import kbController

controller = StateMachine(
    { 
        'init': init, 
        'unlocking': unlocking, 
        'unlocked': unlocked, 
        'openDoor': openDoor, 
        'locking': locking
    },
    { 
        'requesting': False, 
        'door': False, 
        'engine': 0,
        'timeout': 10,
        'tries': 0
    },
    'init'
)

kbController.start()
controller.start()

kbController.join()
controller.join()
