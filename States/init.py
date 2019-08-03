from Core.controller import State

_initConditions = [
    { 'nextState': 'unlocking', 'conditions': { 'requesting': True } }
]

def _initFunc(variables):
    return variables

init = State('Inicial', _initFunc, _initConditions)
