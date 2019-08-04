class EngineController:
    def __init__(self):
        self.rotation = 0
        self.working = 0

    def start(self):
        self.working = 1

    def stop(self):
        self.working = 0

    def setRotate(self, rotation):
        options = { 'clockwise': 1, 'anticlockwise': -1  }
        self.rotation = options[rotation]
