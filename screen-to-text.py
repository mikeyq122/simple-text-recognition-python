from tkinter import Tk, Label, Button, Text
import tkinter
from pynput import keyboard
import sys
import get_pos
from time import sleep
import pyautogui
from PIL import Image
import pytesseract
import pyperclip
import re

if len(sys.argv) > 1:
    multi = sys.argv[1]
else:
    multi = 4
multi = int(multi)

run = ""
GUI = ""
m = ""
r = ""
x = []
y = []
text = ""

def copy():

    global r

    r.clipboard_clear()
    r.clipboard_append(text)
    #print("text")

def setpos():
    global x
    pos = len(x) + 1
    if (pos < 3):
        get_pos.getkey()
        global y
        lx, ly = pyautogui.position()
        x.append(lx)
        y.append(ly)

        global GUI
        if len(x) == 1:
            #print(111)
            GUI.custom_button['text'] = "Position Set"
        elif len(x) == 2:
            if (x[0] < x[1]):
                x = [x[0], x[1]]
            else:
                x = [x[1], x[0]]
            if (y[0] < y[1]):
                y = [y[0], y[1]]
            else:
                y = [y[1], y[0]]

            GUI.custom_button['text'] = "DONE"
            ss = pyautogui.screenshot()
            ss = ss.crop((x[0], y[0], x[1], y[1]))
            ss = ss.resize((ss.width * multi, ss.height * multi))
            #ss.save(r'~/Desktop/assets/ss.png')
            global text
            text = pytesseract.image_to_string(ss, lang="eng")
            #text = re.findall(r'\w+', text)
            T = GUI.output = Text(m)
            T.insert(tkinter.END, text)
            GUI.output.pack()
            GUI.Copy = Button(m, text="Copy to Clipboard", command=copy)
            GUI.Copy.pack()




class MyFirstGUI:
    def __init__(self, master):
        global GUI
        global m
        GUI = self
        m = master
        self.master = master
        master.title("SMART SCREENSHOT")

        self.label = Label(master, text="SMART SCREENSHOT")
        self.label.pack()

        self.infotext = Label(master, text="positions not set")
        self.infotext.pack()

        self.custom_button = Button(master, text="Set pos", command=self.setpos)
        self.custom_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()


    def greet(self):
        print("Greetings!")

    def copy(self):
        print("FGHJK")

    def setpos(self):
        if (self.custom_button['text'] != "DONE"):
            self.custom_button['text'] = "press any key to set"

        global run
        run = "setpos()"
        #self.custom_button['text'] = "Set pos"




root = Tk()
r = root
my_gui = MyFirstGUI(root)

def task():
    root.after(250, task)  # reschedule event in 0.25 seconds
    global run
    exec(run)
    run=""

root.after(2000, task)

root.mainloop()

