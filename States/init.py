from threading import currentThread
from Core.controller import State
from KeyboardController.controller import kbController

_initConditions = [
    { 'nextState': 'locked', 'conditions': { } }
]

def _initFunc(variables):
    return variables

init = State('init', _initFunc, _initConditions)
