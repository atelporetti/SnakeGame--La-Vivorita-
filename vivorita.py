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
        rango_x, rango_y = int(constantes.CANVA_WIDTH-15), int(constantes.CANVA_HEIGHT-15)
        while True:
            x, y = random.randint(0, rango_x), random.randint(0, rango_y)
            if (x and y) % 20 == 0:
                break
        return (x, y)

class VivoritaPantalla(Canvas, Bloque):
    def __init__(self, master):
        Canvas.__init__(self, master)
        Bloque.__init__(self)
        self.master = master
        self.config(bg=constantes.color_fondo, width=constantes.CANVA_WIDTH, height=constantes.CANVA_HEIGHT, highlightthickness=0)
        self.grid(row=1, column=0, columnspan=2)

        self.puntaje = 0
        self.cuerpo_coordenadas = [(300, 300), (300, 300)]
        self.comida_coordenadas = self.genera_comida_aleatoria()
        self.color_cabeza = constantes.color_cabeza
        self.color_cuerpo = constantes.color_cuerpo
        self.velocidad_X = 1
        self.velocidad_Y = 1
        self.direcciones_posibles = constantes.DIRECCIONES_FLECHAS
        self.direccion = random.choice(self.direcciones_posibles)
        self.bind_all('<Key>', self.presiona_tecla)

        self.cargar_imagenes_cuerpo_cabeza()
        self.cargar_bordes()
        self.cargar_vivorita()
        self.cargar_comida()
        self.mover_vivorita()
        self.after(constantes.INTERVALO_TIEMPO_MS, self.realizar_acciones)

    def cargar_imagenes_cuerpo_cabeza(self):

        #
        self.create_text(
            35, 12, text=f"Score: {self.puntaje}", tag="score", fill="#fff", font=10
        )
        #

        self.cabeza = PhotoImage(file=constantes.cabeza_serpiente)
        self.create_image(-10, -10, image=self.cabeza, tag='bloque_cabeza')
        self.cuerpo = PhotoImage(file=constantes.cuerpo_serpiente)
        self.create_image(-10, -10, image=self.cuerpo, tag='bloque_cuerpo')
        self.comida = PhotoImage(file=constantes.comida)
        self.create_image(-10, -10, image=self.comida, tag='bloque_comida')
        self.hueco = PhotoImage(file=constantes.comida)
        self.create_image(-10, -10, image=self.hueco, tag='bloque_hueco')

    def cargar_bordes(self):
        self.create_rectangle(5,5,constantes.CANVA_WIDTH-5,constantes.CANVA_HEIGHT-5, outline=constantes.color_cuerpo)

    def cargar_vivorita(self):
        for coordenada_X, coordenada_Y in self.cuerpo_coordenadas:
            self.create_image(coordenada_X, coordenada_Y, image=self.cuerpo, tag='cuerpo')
    
    def cargar_comida(self):
        self.create_image(*self.comida_coordenadas, image=self.comida, tag='comida')
    
    def mover_vivorita(self):
        coordenada_X, coordenada_Y = self.cuerpo_coordenadas[0]
        if self.direccion == 'Right':
            nueva_coordenada_cabeza = (coordenada_X + constantes.VELOCIDAD, coordenada_Y) # + constantes.VELOCIDAD
        elif self.direccion == 'Left':
            nueva_coordenada_cabeza = (coordenada_X - constantes.VELOCIDAD, coordenada_Y) # + constantes.VELOCIDAD
        elif self.direccion == 'Up':
            nueva_coordenada_cabeza = (coordenada_X, coordenada_Y - constantes.VELOCIDAD) # + constantes.VELOCIDAD
        elif self.direccion == 'Down':
            nueva_coordenada_cabeza = (coordenada_X, coordenada_Y + constantes.VELOCIDAD) # + constantes.VELOCIDAD
        # Agrega la primera posicion de la 
        self.cuerpo_coordenadas = [nueva_coordenada_cabeza] + self.cuerpo_coordenadas[:-1]
        # Empareza las imagenes de los segmentos del cuerpo con las nuevas coordenadas, por pares
        for segmento, coordenada in zip(self.find_withtag('cuerpo'), self.cuerpo_coordenadas):
            self.coords(segmento, coordenada)
    
    def realizar_acciones(self):
        if self.comprobar_colisiones():
            print('Fin del juego!')
            return
        self.colisiona_comida()
        self.mover_vivorita()
        self.after(constantes.INTERVALO_TIEMPO_MS, self.realizar_acciones)

    def comprobar_colisiones(self):
        coordenada_X, coordenada_Y = self.cuerpo_coordenadas[0]
        # True si se cumplen algunas de las dos condiciones: choque contra las paredes (dos valores, inferior y superior o izquierdo y derecho) o contra su cuerpo
        return(coordenada_X in (0, constantes.CANVA_WIDTH) or coordenada_Y in (0, constantes.CANVA_HEIGHT)
        or (coordenada_X, coordenada_Y) in self.cuerpo_coordenadas[1:])

    def presiona_tecla(self, evento):
        nueva_direccion = evento.keysym
        # Set de opuestos, no tienen orden
        direcciones_opuestas = ({'Left', 'Right'}, {'Up', 'Down'})
        if (nueva_direccion in self.direcciones_posibles
            and {self.direccion, nueva_direccion} not in direcciones_opuestas):
            self.direccion = nueva_direccion

    def colisiona_comida(self):
        if self.comida_coordenadas == self.cuerpo_coordenadas[0]:
            self.puntaje += 1
            # Agrega la cola de la serpiente una vez, que luego sera quitada con la funcion mover_vivorita()
            self.cuerpo_coordenadas.append(self.comida_coordenadas)
            self.comida_coordenadas = self.genera_comida_aleatoria()
            self.coords(self.find_withtag('comida'), *self.comida_coordenadas)
            # Crea un bloque en la ultima posicion de la vivorita
            #self.create_image(*self.cuerpo_coordenadas[-1], image=self.cuerpo, tag='bloque_cuerpo')
            # Actualiza el puntaje
            puntaje = self.find_withtag('score')
            self.itemconfigure(puntaje, text=f'Score: {self.puntaje}', tag='score')

    def genera_comida_aleatoria(self):
            while True:
                # Se les resta 1 para que no queden ubicadas en el borde del mapa y se considere perdido el juego
                coordenada_X = random.randint(1, constantes.CELL_CANVA_WIDTH-1) * constantes.CELL_SIZE
                coordenada_Y = random.randint(1, constantes.CELL_CANVA_HEIGHT-1) * constantes.CELL_SIZE
                coordenadas_comida = (coordenada_X, coordenada_Y)
                if (coordenadas_comida not in self.cuerpo_coordenadas): #or (not coordenada_X in (0, constantes.CANVA_WIDTH) and not coordenada_Y in (0, constantes.CANVA_HEIGHT))
                    return coordenadas_comida



root = Tk()

vivorita = VivoritaPantalla(root)
root.mainloop()