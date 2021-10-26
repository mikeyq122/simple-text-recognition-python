from pynput import keyboard
key = ""
def getkey():
    print("getting key")
    def on_press(input):

        global key
        key=str(input)
        return False

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
    global key
    print("got key")
    return key