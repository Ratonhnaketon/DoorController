from threading import currentThread
from Core.controller import State
from KeyboardController.controller import kbController

_lockedConditions = [
    { 'nextState': 'unlocking', 'conditions': { 'requesting': True } }
]

def _lockedFunc(variables):
    if (kbController.getBuffer() == '1234'):
        variables['requesting'] = True
    return variables

locked = State('locked', _lockedFunc, _lockedConditions)