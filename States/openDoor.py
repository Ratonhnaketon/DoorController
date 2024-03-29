from Core.controller import State

_openDoorConditions = [
    { 'nextState': 'unlocked', 'conditions': { 'isDoorOpen': False } }
]

def _openDoorFunc(variables):
    variables['timeout'] = 10
    return variables

openDoor = State('openDoor', _openDoorFunc, _openDoorConditions)