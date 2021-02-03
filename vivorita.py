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

    def coordenadas_aleatorias(self):
        rango_x, rango_y = int(constantes.WINDOW_WIDTH), int(constantes.WINDOW_HEIGHT)
        while True:
            x, y = random.randint(0, rango_x), random.randint(0, rango_y)
            if (x and y) % 20 == 0:
                break
        return (x, y)

class Vivorita(Canvas, Bloque):
    def __init__(self, master):
        Canvas.__init__(self, master)
        Bloque.__init__(self)
        self.master = master
        self.config(bg='blue', width=constantes.WINDOW_WIDTH-40, height=constantes.WINDOW_HEIGHT-82, highlightthickness=0)
        self.grid(row=1, column=0, columnspan=2)
        self.cabeza_coordenadas = [(370, 350)]
        self.cuerpo_coordenadas = [(350, 350), (330, 350)]
        self.comida_coordenadas = (self.coordenadas_aleatorias())
        self.color_cabeza = constantes.color_cabeza
        self.color_cuerpo = constantes.color_cuerpo
        self.velocidad_X = 1
        self.velocidad_Y = 1
        self.cargar_imagenes_cuerpo_cabeza()
        self.cargar_vivorita()
        self.cargar_comida()
        self.cargar_bordes()

    def cargar_imagenes_cuerpo_cabeza(self):
        self.cabeza = PhotoImage(file=constantes.cabeza_serpiente)
        self.create_image(110, 350, image=self.cabeza, tag='bloque_cabeza')
        self.cuerpo = PhotoImage(file=constantes.cuerpo_serpiente)
        self.create_image(130, 350, image=self.cuerpo, tag='bloque_cuerpo')
        self.comida = PhotoImage(file=constantes.comida)
        self.create_image(210, 350, image=self.comida, tag='bloque_comida')
    
    def cargar_bordes(self):
        self.create_rectangle(0,0,670,6100, outline=constantes.color_obstaculo)

    def cargar_vivorita(self):
        for coordenada_X, coordenada_Y in self.cabeza_coordenadas:
            self.create_image(coordenada_X, coordenada_Y, image=self.cuerpo, tag='cuerpo')
    
    def cargar_comida(self):
        self.create_image(*self.comida_coordenadas, image=self.comida, tag='comida')





""" root = Tk()

vivorita = Vivorita(root) """