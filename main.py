from distutils.cmd import Command
from msilib.schema import CheckBox
from pydoc import stripid
import random
import string
from tkinter import *
from tkinter import ttk

tkWindow = Tk()  
tkWindow.geometry('250x150')  
tkWindow.title('MakePass')
tkWindow.resizable(False,False)

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

password = []

def passgen():

    random.shuffle(characters)

    for i in range(length.get()):
        password.append(random.choice(characters))

    random.shuffle(password)

    passinput()

def changeState():
    if (GenButton['state'] == NORMAL):
        GenButton['state'] = DISABLED
    else:
        GenButton['state'] = NORMAL

def passinput():
    passEntry.insert(0, "".join(password))
    changeState()

def ShowPass():
    if (passEntry['show'] == "*"):
        passEntry['show'] = ""
    else:
        passEntry["show"] = "*"

lengthLabel = Label(tkWindow, text="Password length:").grid(row=0, column=0)
length = IntVar()
lengthEntry = Entry(tkWindow, textvariable=length).grid(row=0, column=1)

passEntry = Entry(tkWindow, show="*")
passEntry.grid(row=1, column=1)

GenButton = Button(tkWindow, text="Generate", command=passgen, state=NORMAL)
GenButton.grid(row=1, column=0) 

ShowPassBox = Checkbutton(tkWindow, text="Show Password", command=ShowPass).grid(row=2, column=1)

versionInfo = Label(tkWindow, text="Version 1.2.0").place(x=178, y=110)
versionInfo = Label(tkWindow, text="Bruhteam - Makepass").place(x=130, y=130)

tkWindow.mainloop()
