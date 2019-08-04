from Core.controller import StateMachine 
from KeyboardController.controller import kbController
from ServerController.controller import svrController

from States.init import init
from States.locking import locking
from States.openDoor import openDoor
from States.unlocked import unlocked
from States.unlocking import unlocking


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


# kbController.start()
controller.start()
svrController.config(5000, False, False)
svrController.start()
# kbController.join()
