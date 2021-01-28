try:
    from tkinter import *
except:
    from Tkinter import *

class Puntaje:
    def __init__(self, master):
        self.contador = StringVar(master, "0")
        self.maximo = StringVar(master, "0")

    def aumenta(self):
        puntaje = int(self.contador.get()) + 1
        maximo = max(puntaje, int(self.maximo.get()))
        self.contador.set(str(puntaje))
        self.maximo.set(str(maximo))

    def reset(self):
        self.contador.set("0")
