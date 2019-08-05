from time import sleep
from threading import Thread
from DoorSensorController.controller import doorSensor

class StateMachine(Thread):
    def __init__(self, states, variables, initState):
        Thread.__init__(self)
        self.stateIndex = initState # string
        self.states = states        # dict
        self.variables = variables  # dict
        self.actualState = initState 
        self.initVariables = variables.copy()
        self.initState = initState
        self.nextState = initState

    def run(self):
        print('Starting state machine...\r')
        
        while True:
            self.variables['isDoorOpen'] = doorSensor.doorIsOpen
            self.resetVariablesIfInitState()
            self.getActualState()
            print('Actual state: {0}\r'.format(self.actualState.name))
            print('Running state...\r')
            self.executeState()
            self.checkConditions()
            print('Changing state...\r')
            self.changeState()
            sleep(1)

    def resetVariablesIfInitState(self):
        if self.stateIndex == self.initState:
            self.variables = self.initVariables.copy() 

    def getActualState(self):
        self.actualState = self.states[self.stateIndex]

    def executeState(self):
        self.variables = self.actualState.func(self.variables)        

    def checkConditions(self):
        self.nextState = self.actualState.name
        for condition in self.actualState.conditions:
            if condition['conditions'] == {}:
                self.nextState = condition['nextState']
                return
            for key, value in condition['conditions'].iteritems():
                if not self.variables[key] == value:
                    break
            else:
                self.nextState = condition['nextState']
                return
            
    def changeState(self):
        self.stateIndex = self.nextState

class State:
    def __init__(self, name, func, conditions):
        self.name = name                # string
        self.func = func                # function
        self.conditions = conditions    # dict