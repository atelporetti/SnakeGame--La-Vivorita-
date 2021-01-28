try:
    from tkinter import *
except:
    from Tkinter import *
from ventana_inicio import Inicio
import constantes

class PantallaJuego(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        #Frame.configure(self,bg='blue', width=800, height=800)
        self.master = master
        self.config(background='yellow', width=constantes.WINDOW_WIDTH, height=constantes.WINDOW_HEIGHT)  # tcross, cross, dotbox
        self.grid(sticky='nsew')
        #self.rowconfigure((0, constantes.filas), weight=1)
        #self.columnconfigure((0, constantes.columnas), weight=1)

        self._canvas = Canvas(master)
        self._canvas.config(bg='blue', width=720, height=680)
        self._canvas.grid(row=0, column=0)
        self.label = Label(self, text="PANTALLA JUEGO", font=(constantes.tipografia, 10, "bold")).grid(row=0, column=0, padx=10, pady=10)

        self.button = Button(self, text="Volver a jugar",command=lambda: self.master.cambia_frame(Inicio), font=(constantes.tipografia, 10, "bold")).grid(row=0, column=1, padx=10, pady=10)
