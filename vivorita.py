try:
    from tkinter import *
except:
    from Tkinter import *
import constantes
import random

class Bloque():
    x = 0
    y = 0
    color = ''
    grosor = constantes.CELL_SIZE

    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y

    def coordenadas_aleatorias():
        rango_x, rango_y = int(constantes.WINDOW_WIDTH - 1), int(constantes.WINDOW_HEIGHT - 1)
        x, y = random.randint(0, rango_x), random.randint(0, rango_y)
        return x, y

class Vivorita(Bloque):
    def __init__(self, master, color, color_cabeza, x, y):
        Bloque.__init__(self, color, x, y)
        self.master = master
        self.cabeza_coordenadas = [()]
        self.cuerpo_coords = [()]
        self.color_cabeza = color_cabeza
        self.color_cuerpo = color
        self.velocidad_X = 1
        self.velocidad_Y = 1
