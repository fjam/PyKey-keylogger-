from pynput.mouse import Controller
from pynput.keyboard import Controller

def controlMouse():
    mouse = Controller()
    mouse.position = (10, 20)


def contorlKeyboard():
    keyboard = Controller()
    keyboard.type("testing from keyboard input")

contorlKeyboard()