from threading import Thread

class KeyboardController(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.__buffer = ''

    def run(self):
        global buffer
        while True:
            buffer = str(raw_input())
            self.__buffer = buffer

    def getBuffer(self):
        buffer = str(self.__buffer)
        self.__buffer = ''
        return buffer

kbController = KeyboardController()
