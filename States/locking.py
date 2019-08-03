from Core.controller import State

_lockingConditions = [
    { 'nextState': 'init', 'conditions': { 'engine': 0 } }
]

def _lockingFunc(variables):
    return variables

locking = State('Trancando', _lockingFunc, _lockingConditions)