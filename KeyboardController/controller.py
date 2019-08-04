from threading import Thread
import sys, tty, termios

class KeyboardController(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.__buffer = ''
        self.daemon = True

    def run(self):
        global buffer
        while True:
            buffer = getChar(4)
            self.__buffer = buffer

    def getBuffer(self):
        buffer = str(self.__buffer)
        self.__buffer = ''
        return buffer

def getChar(quantity):
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(quantity)
        print(ch)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

kbController = KeyboardController()


