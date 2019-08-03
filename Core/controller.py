from time import sleep

class StateMachine:
    def __init__(self, states, variables, initState):
        self.stateIndex = initState # string
        self.states = states        # dict
        self.variables = variables  # dict
        self.initVariables = variables.copy()

    def start(self):
        while True:
            if self.stateIndex == 0:
                self.variables == self.initVariables
                
            actualState = self.getActualState()
            self.executeState(actualState)

            nextState = self.checkConditions(actualState.conditions) 
            self.changeState(nextState)
            sleep(1)


    def getActualState(self):
        actualState = self.states[self.stateIndex]
        print("Actual state: {0}".format(actualState.name))
        return actualState

    def executeState(self, actualState):
        print("Running state...")
        changedVariables = actualState.func()
        for key, value in changedVariables.iteritems():
            self.variables[key] = value

    def checkConditions(self, actualStateConditions):
        for condition in actualStateConditions:
            for key, value in condition['conditions'].iteritems():
                if not self.variables[key] == value:
                    break
            else:
                return condition['nextState']
        return self.stateIndex

    def changeState(self, nextState):
        print("Changing state...")
        self.stateIndex = nextState

class State:
    def __init__(self, name, func, conditions):
        self.name = name                # string
        self.func = func                # function
        self.conditions = conditions    # dict
