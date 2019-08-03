from Core.controller import State

_initConditions = [
    { 'nextState': 'unlocking', 'conditions': { 'requesting': True } }
]

def _initFunc():
    return {}

init = State('Inicial', _initFunc, _initConditions)
