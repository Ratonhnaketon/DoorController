from Core.controller import State

_openDoorConditions = [
    { 'nextState': 'unlocked', 'conditions': { 'door': False } }
]

def _openDoorFunc():
    return {} 

openDoor = State('Porta aberta', _openDoorFunc, _openDoorConditions)