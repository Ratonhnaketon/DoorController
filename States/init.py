from threading import currentThread
from Core.controller import State
from KeyboardController.controller import kbController

_initConditions = [
    { 'nextState': 'unlocking', 'conditions': { 'requesting': True } }
]

def _initFunc(variables):
    if (kbController.getBuffer() == '1234'):
        variables['requesting'] = True
    return variables

init = State('init', _initFunc, _initConditions)
