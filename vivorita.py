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

    """ def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y """

    def coordenadas_aleatorias():
        rango_x, rango_y = int(constantes.WINDOW_WIDTH - 1), int(constantes.WINDOW_HEIGHT - 1)
        x, y = random.randint(0, rango_x), random.randint(0, rango_y)
        return x, y

class Vivorita(Canvas, Bloque):
    def __init__(self, master):
        Canvas.__init__(self, master)
        Bloque.__init__(self)
        self.master = master
        self.config(bg='blue',width=constantes.WINDOW_WIDTH, height=constantes.WINDOW_HEIGHT, highlightthickness=0)
        self.grid(row=1, column=0, columnspan=2)
        self.cabeza_coordenadas = [(350, 350), (330, 350)]
        self.cuerpo_coordenadas = [self.coordenadas_aleatorias]
        self.color_cabeza = constantes.color_cabeza
        self.color_cuerpo = constantes.color_cuerpo
        self.velocidad_X = 1
        self.velocidad_Y = 1
        self.cargar_imagenes_cuerpo_cabeza()
        self.cargar_vivorita()
        #self.cargar_comida()

    def cargar_imagenes_cuerpo_cabeza(self):
        self.cabeza = PhotoImage(file=constantes.cabeza_serpiente)
        self.create_image(110, 350, image=self.cabeza, tag='bloque_cabeza')
        self.cuerpo = PhotoImage(file=constantes.cuerpo_serpiente)
        self.create_image(130, 350, image=self.cuerpo, tag='bloque_cuerpo')
        
    def cargar_vivorita(self):
        for coordenada_X, coordenada_Y in self.cabeza_coordenadas:
            self.create_image(coordenada_X, coordenada_Y, image=self.cuerpo, tag='cuerpo')
    
    def cargar_comida(self):
        for coordenada_X, coordenada_Y in self.cuerpo_coordenadas:
        #coordenada_X, coordenada_Y = self.coordenadas_aleatorias()
            self.create_image(coordenada_X, coordenada_Y, image=self.cuerpo, tag='comida')





""" root = Tk()

vivorita = Vivorita(root) """