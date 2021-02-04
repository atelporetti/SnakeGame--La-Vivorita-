try:
    from tkinter import *
except:
    from Tkinter import *
from ventana_inicio import Inicio
import constantes, ventana_inicio, pygame, os, platform
from vivorita import VivoritaPantalla

class PantallaJuego(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        #Frame.configure(self,bg='blue', width=800, height=800)
        self.master = master
        self._frame = Frame(master)
        self.config(background='yellow', width=constantes.WINDOW_WIDTH, height=constantes.WINDOW_HEIGHT)  # tcross, cross, dotbox
        self.grid(row=0, column=0, sticky='nsew')
        self.puntaje = 0
        self.nivel = 0
        #self.rowconfigure((0, 1), weight=1)
        self.columnconfigure((0, 1), weight=1)

        #self.controller = controller
        #self.nombre = controller.nombre
        #self.velocidad = controller.velocidad
        #self.dificultad = controller.dificultad
        self.nombre = StringVar()
        self.velocidad = IntVar()
        self.dificultad = IntVar()

        self.lb_nombre = Label(self, text=f'Puntaje de {self.nombre}: {self.puntaje}. Nivel: {self.nivel}', font=(constantes.tipografia, 6, "bold"))
        self.lb_nombre.grid(row=0, column=0, padx=0, pady=0)
        self.lb_nombre.config(bg=constantes.color_fondo, fg='white',
                            justify='left',
                            font=(constantes.tipografia, 12))
        self.button = Button(self, text="Volver a jugar",command=lambda:[self.master.cambia_frame(Inicio, self.master)], font=(constantes.tipografia, 6, "bold"))
        self.button.grid(row=0, column=1, sticky='nsew',padx=0, pady=0)
        self.button.config(bg=constantes.color_fondo, fg='white',
                            justify='left',
                            font=(constantes.tipografia, 12))

        # ------------------------------
        self.vivora = VivoritaPantalla(self)
        #self._canvas.create_rectangle(360, 360, 380, 380, fill=constantes.color_cabeza)
                
        self.configuracion_tkinter_pygame()
        self.reproducir_musica()


        #self.snake = Vivorita(self._canvas, constantes.color_cuerpo, constantes.color_cabeza, 360, 360)
        #self.snake.grosor
        #self.snake.block_coords

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