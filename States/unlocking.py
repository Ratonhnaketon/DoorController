from Core.controller import State

_unlockingConditions = [
    { 'nextState': 'unlocked', 'conditions': { 'engine': 0 } }, 
]

def _unlockingFunc(variables):
    variables['requesting'] = False
    return variables

unlocking = State('unlocking', _unlockingFunc, _unlockingConditions)
