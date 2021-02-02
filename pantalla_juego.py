try:
    from tkinter import *
except:
    from Tkinter import *
from ventana_inicio import Inicio
import constantes, ventana_inicio, pygame, os, platform

class PantallaJuego(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        #Frame.configure(self,bg='blue', width=800, height=800)
        self.master = master
        self._frame = Frame(master)
        self.config(background='yellow', width=constantes.WINDOW_WIDTH, height=constantes.WINDOW_HEIGHT)  # tcross, cross, dotbox
        self.grid(sticky='nsew')
        self.puntaje = 0
        self.nivel = 0
        self.rowconfigure((0, constantes.filas), weight=1)
        self.columnconfigure((0, constantes.columnas), weight=1)
        self.nombre = ''
        self.lb_nombre_jugador = Entry(self, textvariable=self.nombre)
        self.lb_nombre_jugador.grid(row=0, column=0)
        self.lb_nombre = Label(self, text=f'Puntaje de : {self.lb_nombre_jugador}. Nivel: {self.nivel}', font=(constantes.tipografia, 6, "bold"))
        self.lb_nombre.grid(row=0, column=1, padx=10, pady=10)
        self.label = Label(self, text=f'Puntaje de : {self.nombre}', font=(constantes.tipografia, 6, "bold"))
        self.label.grid(row=1, column=0, padx=10, pady=10)
        self.button = Button(self, text="Volver a jugar",command=lambda:[self.master.cambia_frame(Inicio, self.master), ], font=(constantes.tipografia, 6, "bold"))
        self.button.grid(row=1, column=1, padx=10, pady=10)

        self._canvas = Canvas(self)
        self._canvas.config(bg='blue', width=constantes.WINDOW_WIDTH, height=(constantes.WINDOW_HEIGHT))
        self._canvas.grid(row=2, column=0, sticky='nsew') #
        self.label = Label(self._canvas, text=f'Puntaje de : {self.nombre}', font=(constantes.tipografia, 6, "bold")).grid(row=1, column=0, padx=10, pady=10)
        
        self.board=Canvas(self, width=constantes.WINDOW_WIDTH, height=constantes.WINDOW_HEIGHT, background=constantes.color_fondo)
        self.board.grid()
        self.snake=self.board.create_rectangle(1,1,11,11,fill=constantes.color_cabeza)
        self.configuracion_tkinter_pygame()
        self.reproducir_musica()

    #Por si hiciera falta
    def configuracion_tkinter_pygame(self):
        os.environ['SDL_WINDOWID'] = str(self.winfo_id())
        if platform.system == "Windows":
            os.environ['SDL_VIDEODRIVER'] = 'windib'

    def reproducir_musica(self):
        pygame.mixer.pre_init(44100, -16, 2, 2048)
        pygame.mixer.init()
        pygame.mixer.music.load(constantes.musica_en_juego)
        pygame.mixer.music.set_volume(0.4)
        pygame.mixer.music.play(-1)