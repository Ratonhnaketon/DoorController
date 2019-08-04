from Core.controller import State

_unlockedConditions = [
    { 'nextState': 'openDoor', 'conditions': { 'door': True } }, 
    { 'nextState': 'locking', 'conditions': { 'timeout': 0 } }, 
]

def _unlockedFunc(variables):
    variables['timeout'] -= 1 
    return variables

unlocked = State('unlocked', _unlockedFunc, _unlockedConditions)
