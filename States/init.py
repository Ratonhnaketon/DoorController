from Core.controller import State

_initConditions = [
    { 'nextState': 'locked', 'conditions': { } }
]

def _initFunc(variables):
    return variables

init = State('init', _initFunc, _initConditions)
