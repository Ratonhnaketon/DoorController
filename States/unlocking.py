from Core.controller import State

_unlockingConditions = [
    { 'nextState': 'unlocked', 'conditions': { 'engine': 0 } }, 
    { 'nextState': 'init', 'conditions': { 'engine': 0, 'tries': 3 } } 
]

def _unlockingFunc(variables):
    return variables

unlocking = State('unlocking', _unlockingFunc, _unlockingConditions)
