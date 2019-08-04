from Core.controller import State

_unlockedConditions = [
    { 'nextState': 'openDoor', 'conditions': { 'door': True } }, 
    { 'nextState': 'locking', 'conditions': { 'timeout': 0 } }, 
    { 'nextState': 'locking', 'conditions': { 'door': False } } 
]

def _unlockedFunc(variables):
    return variables

unlocked = State('unlocking', _unlockedFunc, _unlockedConditions)
