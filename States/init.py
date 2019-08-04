from Core.controller import State

_initConditions = [
    { 'nextState': 'unlocking', 'conditions': { 'requesting': True } }
]

def _initFunc(variables):
    return variables

init = State('init', _initFunc, _initConditions)
