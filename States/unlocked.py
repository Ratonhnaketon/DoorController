from Core.controller import State

_unlockedConditions = [
    { 'nextState': 'openDoor', 'conditions': { 'door': True } }, 
    { 'nextState': 'locking', 'conditions': { 'timeout': 0 } }, 
    { 'nextState': 'locking', 'conditions': { 'door': False } } 
]

def _unlockedFunc():
    return {} 

unlocked = State('Destrancado', _unlockedFunc, _unlockedConditions)
