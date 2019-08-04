from Core.controller import State
from EngineController.controller import engine
from time import sleep

_unlockingConditions = [
    { 'nextState': 'unlocked', 'conditions': { } }, 
]

def _unlockingFunc(variables):
    engine.rotateCounterClockWise()
    sleep(2)
    engine.stop()
    variables['requesting'] = False
    return variables

unlocking = State('unlocking', _unlockingFunc, _unlockingConditions)
