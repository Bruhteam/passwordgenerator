# Імпорт бібліотек | Libraries importing
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


# Генератор / Generator
def passgen():

    # Перемішення символів / Character shuffling
    random.shuffle(characters)

    # Генерація пустої ячейки пароля / Password's empty list generating
    password = []
    # Генерація пароля з заданою довжиною / Password generation
    for i in range(length.get()):
        password.append(random.choice(characters))

    # Перемішення символів у паролі / Shuffling characters in passwortd
    random.shuffle(password)

    # Вивід паролю / Password output
    print("".join(password))

# хз / idk
genpass = StringVar()

# Ввести довжину пароля / Enter Password length
lengthLabel = Label(tkWindow, text="Password length:").grid(row=0, column=0)
length = IntVar()
lengthEntry = Entry(tkWindow, textvariable=length).grid(row=0, column=1)

# Генерація пароля / Password Generation Button
GenButton = Button(tkWindow, text="Generate", command=passgen).grid(row=1, column=0) 

# Інформація про версію / Version Info
versionInfo = Label(tkWindow, text="Version 0.3.1.2").place(x=170, y=130)

tkWindow.mainloop()