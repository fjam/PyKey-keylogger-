from pynput.mouse import Listener

def writeToFile(x, y):
    print("Position of Current mouse {0}".format((x,y)))

with Listener(on_move=writeToFile) as l:
    l.join() 