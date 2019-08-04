from Core.controller import State
from main import engine
from time import sleep

_lockingConditions = [
    { 'nextState': 'init', 'conditions': { } }
]

def _lockingFunc(variables):
    engine.rotateClockWise()
    sleep(2)
    engine.stop()
    return variables

locking = State('locking', _lockingFunc, _lockingConditions)