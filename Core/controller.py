from time import sleep

class StateMachine:
    def __init__(self, states, variables, initState):
        self.stateIndex = initState # string
        self.states = states        # dict
        self.variables = variables  # dict
        self.actualState = initState 
        self.initVariables = variables.copy()
        self.initState = initState
        self.nextState = initState

    def start(self):
        while True:
            self.resetVariablesIfInitState()
            self.getActualState()
            self.executeState()
            self.checkConditions() 
            self.changeState()
            sleep(1)

    def resetVariablesIfInitState(self):
        if self.stateIndex == self.initState:
            self.variables = self.initVariables 

    def getActualState(self):
        self.actualState = self.states[self.stateIndex]
        print('Actual state: {0}'.format(self.actualState.name))

    def executeState(self):
        print('Running state...')
        self.variables = self.actualState.func(self.variables)        

    def checkConditions(self):
        self.nextState = self.actualState.name
        for condition in self.actualState.conditions:
            for key, value in condition['conditions'].iteritems():
                if not self.variables[key] == value:
                    break
            else:
                self.nextState = condition.nextState
            
    def changeState(self):
        print('Changing state...')
        self.stateIndex = self.nextState

class State:
    def __init__(self, name, func, conditions):
        self.name = name                # string
        self.func = func                # function
        self.conditions = conditions    # dict