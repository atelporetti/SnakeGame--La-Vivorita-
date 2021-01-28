try:
    from tkinter import *
except:
    from Tkinter import *
import constantes
import random
master = Tk()

class Bloque():
    x = 0
    y = 0
    color = ''
    grosor = 1
    def __init__(self, master, color, x, y):
        self.master = master
        self.color = color
        self.x = x
        self.y = y

    def coordenadas_aleatorias():
        rango_x, rango_y = int(constantes.WINDOW_WIDTH - 1), int(constantes.WINDOW_HEIGHT - 1)
        x, y = random.randint(0, rango_x), random.randint(0, rango_y)
        return x, y

class Vivorita(Bloque):
    def __init__(self, master, color, x, y):
        Bloque.__init__(self, master, color, x, y)
        self.master = master
        self.cabeza_coordenadas = set([(X, Y)])
        self.color = color
        self.velocidad_X = 1
        self.velocidad_Y = 1
        self.cola = []
        self.block_coords = set([(x, y)])

canvas_width = 440
canvas_height = 440
w = Canvas(master, 
           width=canvas_width,
           height=canvas_height)
w.pack()

y = int(canvas_height / 2)
w.create_line(0, y, canvas_width, y, fill="#476042")
w.create_rectangle()

mainloop()