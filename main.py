# Імпорт бібліотек | Libraries importing
from pydoc import stripid
import random
import string
from tkinter import *
from tkinter import ttk

from pyautogui import sleep

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
    print("".join(password))
    passinput()
    switch()

def switch():
    if GenButton["state"] == "NORMAL":
        GenButton["state"] = "DISABLED"

def passinput():
    passEntry.insert(0, "")
    passEntry.insert(0, "".join(password))
# Ввести довжину пароля / Enter Password length
lengthLabel = Label(tkWindow, text="Password length:").grid(row=0, column=0)
length = IntVar()
lengthEntry = Entry(tkWindow, textvariable=length).grid(row=0, column=1)

passEntry = Entry(tkWindow)
passEntry.grid(row=1, column=1)

# Генерація пароля / Password Generation Button
GenButton = Button(tkWindow, text="Generate", command=passgen, state=NORMAL)
GenButton.grid(row=1, column=0) 
# Інформація про версію / Version Info
versionInfo = Label(tkWindow, text="Version 1.0.1").place(x=178, y=110)
versionInfo = Label(tkWindow, text="Bruhteam - Makepass").place(x=130, y=130)

tkWindow.mainloop()