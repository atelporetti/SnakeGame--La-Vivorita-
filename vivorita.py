try:
    from tkinter import *
except:
    from Tkinter import *
import constantes, random , pygame, time



class VivoritaPantalla(Canvas):
    def __init__(self, master):
        Canvas.__init__(self, master)
        self.master = master
        self.config(bg=constantes.color_fondo, width=constantes.CANVA_WIDTH, height=constantes.CANVA_HEIGHT, highlightthickness=0)
        self.grid(row=1, column=0, columnspan=2)

        self.puntaje = 0
        self.nivel = 1
        self.tiempo_juego_inicio = time.time()
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
        self.cargar_vivorita()
        self.cargar_comida()
        self.mover_vivorita()
        self.after(constantes.VELOCIDAD, self.realizar_acciones)
        self.reproducir_musica_fondo()

    def cargar_imagenes_cuerpo_cabeza(self):

        #
        self.create_text(
            35, 12, text=f"Score: {self.puntaje}", tag="score", fill="#fff", font=10
        )
        self.cabeza = PhotoImage(file=constantes.cabeza_serpiente)
        self.cuerpo = PhotoImage(file=constantes.cuerpo_serpiente)

    def cargar_bordes(self):
        self.create_rectangle(5,5,constantes.CANVA_WIDTH-5,constantes.CANVA_HEIGHT-5, outline=constantes.color_cabeza, width = 4)

    def cargar_vivorita(self):
        for coordenada_X, coordenada_Y in self.cuerpo_coordenadas:
            self.create_image(coordenada_X, coordenada_Y, image=self.cuerpo, tag='cuerpo')
    
    def cargar_comida(self):
        # Creo una lista de imagenes de comidas
        self.comidas = [PhotoImage(file=constantes.comida_violeta), 
                        PhotoImage(file=constantes.comida_roja), 
                        PhotoImage(file=constantes.comida_amarilla), 
                        PhotoImage(file=constantes.comida_azul), 
                        PhotoImage(file=constantes.comida_fucsia), 
                        PhotoImage(file=constantes.comida_naranja), 
                        PhotoImage(file=constantes.comida_verde)]
        self.create_image(*self.comida_coordenadas, image=self.comidas[random.randint(0, len(constantes.comidas))-1], tag='comida')
    
    def mover_vivorita(self):
        coordenada_X, coordenada_Y = self.cuerpo_coordenadas[0]

        if self.direccion == 'Right':
            nueva_coordenada_cabeza = (coordenada_X + constantes.CELL_SIZE, coordenada_Y)
        elif self.direccion == 'Left':
            nueva_coordenada_cabeza = (coordenada_X - constantes.CELL_SIZE, coordenada_Y)
        elif self.direccion == 'Up':
            nueva_coordenada_cabeza = (coordenada_X, coordenada_Y - constantes.CELL_SIZE)
        elif self.direccion == 'Down':
            nueva_coordenada_cabeza = (coordenada_X, coordenada_Y + constantes.CELL_SIZE)
        
        self.cuerpo_coordenadas = [nueva_coordenada_cabeza] + self.cuerpo_coordenadas[:-1]
        # Empareja las imagenes de los segmentos del cuerpo con las nuevas coordenadas, formando ua tupla por pares
        for segmento, coordenada in zip(self.find_withtag('cuerpo'), self.cuerpo_coordenadas):
            self.coords(segmento, coordenada)
    
    def realizar_acciones(self):
        if self.comprobar_colisiones():
            self.fin_juego()
        self.come_comida()
        self.mover_vivorita()
        self.after(constantes.VELOCIDAD, self.realizar_acciones)

    def comprobar_colisiones(self):
        coordenada_X, coordenada_Y = self.cuerpo_coordenadas[0]
        if (coordenada_X, coordenada_Y) in self.cuerpo_coordenadas[1:]:
            self.reproducir_sonido_colision()
            return True
        if self.nivel == 1:
            if coordenada_X == 0:
                self.cuerpo_coordenadas[0] = (constantes.CANVA_WIDTH, coordenada_Y)
            elif coordenada_X == constantes.CANVA_WIDTH:
                self.cuerpo_coordenadas[0] = (0, coordenada_Y)
            elif coordenada_Y == 0:
                self.cuerpo_coordenadas[0] = (coordenada_X, constantes.CANVA_HEIGHT)
            elif coordenada_Y == constantes.CANVA_HEIGHT:
                self.cuerpo_coordenadas[0] = (coordenada_X, 0)
        elif self.nivel == 2:
            # Poner que no se pueda ir y chquee si colisiona en los bordes
            if coordenada_X in (0, constantes.CANVA_WIDTH) or coordenada_Y in (0, constantes.CANVA_HEIGHT):
                self.reproducir_sonido_colision()
                return True
            

    def presiona_tecla(self, evento):
        nueva_direccion = evento.keysym
        # Set de opuestos, no tienen orden
        direcciones_opuestas = ({'Left', 'Right'}, {'Up', 'Down'})
        coordenada_X, coordenada_Y = self.cuerpo_coordenadas[0]
        # Si la cabeza esta en los bordes, que no sea posible cambiar de direccion
        if coordenada_X != 0:
        # Si se apreta una tecla de las flechas o si NO es una direccion opuesta a la que tiene, cambiara de direccion
            if (nueva_direccion in self.direcciones_posibles 
                and {self.direccion, nueva_direccion} not in direcciones_opuestas):
                    self.direccion = nueva_direccion
        if coordenada_X != constantes.CANVA_WIDTH:
            if (nueva_direccion in self.direcciones_posibles 
                and {self.direccion, nueva_direccion} not in direcciones_opuestas):
                    self.direccion = nueva_direccion
        if coordenada_Y != 0:
            if (nueva_direccion in self.direcciones_posibles 
                and {self.direccion, nueva_direccion} not in direcciones_opuestas):
                    self.direccion = nueva_direccion
        if coordenada_Y != constantes.CANVA_HEIGHT:
            if (nueva_direccion in self.direcciones_posibles 
                and {self.direccion, nueva_direccion} not in direcciones_opuestas):
                    self.direccion = nueva_direccion

    def come_comida(self):
        if self.comida_coordenadas == self.cuerpo_coordenadas[0]:
            self.puntaje += 1
            self.reproducir_sonido_comida()
            # Agrega la cola de la serpiente una vez, queda duplicadda la coordenada que luego al moverse una sera quitada con la funcion mover_vivorita()
            self.cuerpo_coordenadas.append(self.cuerpo_coordenadas[-1])
            # Crea un bloque en la ultima posicion de la vivorita
            self.create_image(*self.cuerpo_coordenadas[-1], image=self.cuerpo, tag='cuerpo')
            self.cambia_comida()
            self.comida_coordenadas = self.genera_comida_aleatoria()
            self.coords(self.find_withtag('comida'), *self.comida_coordenadas)

            # Aumenta gradualmente la velocidad cada dos puntos
            if self.puntaje % 2 == 0:
                constantes.MOVIMIENTOS_POR_SEGUNDO += 2
            if self.puntaje == 10:
                self.nivel += 1
                self.cargar_bordes()

            # Actualiza el puntaje
            puntaje = self.find_withtag('score')
            self.itemconfigure(puntaje, text=f'Score: {self.puntaje}', tag='score')

    def genera_comida_aleatoria(self):
            while True:
                # Se les resta 1 para que no queden ubicadas en el borde del mapa y se considere perdido el juego
                coordenada_X = random.randint(1, constantes.CELL_CANVA_WIDTH-1) * constantes.CELL_SIZE
                coordenada_Y = random.randint(1, constantes.CELL_CANVA_HEIGHT-1) * constantes.CELL_SIZE
                coordenadas_comida = (coordenada_X, coordenada_Y)
                if (coordenadas_comida not in self.cuerpo_coordenadas):
                    return coordenadas_comida

    def cambia_comida(self):
        return self.itemconfig(self.find_withtag('comida'), image=self.comidas[random.randint(0, len(constantes.comidas)-1)])
    
    def reproducir_musica_fondo(self):
        pygame.mixer.pre_init(44100, -16, 2, 2048)
        pygame.mixer.init()
        pygame.mixer.music.load(constantes.musica_en_juego)
        pygame.mixer.music.set_volume(0.4)
        pygame.mixer.music.play(-1)

    def reproducir_sonido_comida(self):
        sound_effect = pygame.mixer.Sound(constantes.musica_comida)
        sound_effect.set_volume(0.5)
        pygame.mixer.Sound.play(sound_effect)

    def reproducir_sonido_colision(self):
        sound_effect = pygame.mixer.Sound(constantes.musica_colision)
        sound_effect.set_volume(0.5)
        pygame.mixer.Sound.play(sound_effect)

    def guarda_puntajes(nombre_archivo, nombre):
        """ Guarda la lista de puntajes en el archivo.
        Pre: nombre_archivo corresponde a un archivo válido,
        puntajes corresponde a una lista de tuplas de 3 elementos.
        Post: se guardaron los valores en el archivo,
        separados por comas.
        """
        with open (nombre_archivo, "w") as archivo:
            for puntaje, nombre, tiempo in archivo:
                archivo.write(f'{puntaje} {nombre} {tiempo}\n')

    def fin_juego(self):
        self.tiempo_juego_fin = time.time()
        self.tiempo_juego_total = int(self.tiempo_juego_fin - self.tiempo_juego_inicio)
        self.guarda_puntajes()
        self.grid_remove()
        

""" root = Tk()

vivorita = VivoritaPantalla(root)
root.mainloop() """