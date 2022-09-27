# Імпорт бібліотек | Libraries importing
from distutils.cmd import Command
from msilib.schema import CheckBox
from pydoc import stripid
import random
import string
from tkinter import *
from tkinter import ttk

# Інформація про вікно / Windows' info
tkWindow = Tk()  
tkWindow.geometry('250x150')  
tkWindow.title('MakePass')
tkWindow.resizable(False,False)
# Список символів / Characters list
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

password = []

# Генератор / Generator
def passgen():

    # Перемішення символів / Character shuffling
    random.shuffle(characters)

    # Генерація пустої ячейки пароля / Password's empty list generating
    # Генерація пароля з заданою довжиною / Password generation
    for i in range(length.get()):
        password.append(random.choice(characters))

    # Перемішення символів у паролі / Shuffling characters in passwortd
    random.shuffle(password)

    # Вивід паролю / Password output
    passinput()

# Команда для зміни стану кнопки / Change button state
def changeState():
    if (GenButton['state'] == NORMAL):
        GenButton['state'] = DISABLED
    else:
        GenButton['state'] = NORMAL

# Вивід пароля в ячейку / Password output to Entry Widget
def passinput():
    passEntry.insert(0, "".join(password))
    changeState()

# Команда для показування пароля / Show password command
def ShowPass():
    if (passEntry['show'] == "*"):
        passEntry['show'] = ""
    else:
        passEntry["show"] = "*"

# Ввести довжину пароля / Enter Password length
lengthLabel = Label(tkWindow, text="Password length:").grid(row=0, column=0)
length = IntVar()
lengthEntry = Entry(tkWindow, textvariable=length).grid(row=0, column=1)

# Вивід паролю / Password output
passEntry = Entry(tkWindow, show="*")
passEntry.grid(row=1, column=1)

# Генерація пароля / Password Generation Button
GenButton = Button(tkWindow, text="Generate", command=passgen, state=NORMAL)
GenButton.grid(row=1, column=0) 

# Показати пароль / Show Password Checkbox
ShowPassBox = Checkbutton(tkWindow, text="Show Password", command=ShowPass).grid(row=2, column=1)

# Інформація про версію / Version Info
versionInfo = Label(tkWindow, text="Version 1.2.0").place(x=178, y=110)
versionInfo = Label(tkWindow, text="Bruhteam - Makepass").place(x=130, y=130)

tkWindow.mainloop()