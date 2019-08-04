from Core.controller import State

_openDoorConditions = [
    { 'nextState': 'unlocked', 'conditions': { 'door': False } }
]

def _openDoorFunc(variables):
    return variables

openDoor = State('openDoor', _openDoorFunc, _openDoorConditions)