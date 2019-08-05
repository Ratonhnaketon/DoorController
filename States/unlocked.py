from Core.controller import State
from DoorSensorController.controller import doorSensor

_unlockedConditions = [
    { 'nextState': 'openDoor', 'conditions': { 'isDoorOpen': True } }, 
    { 'nextState': 'locking', 'conditions': { 'timeout': 0 } }, 
]

def _unlockedFunc(variables):
    variables['isDoorOpen'] = doorSensor.doorIsOpen
    variables['timeout'] -= 1 
    return variables

unlocked = State('unlocked', _unlockedFunc, _unlockedConditions)
