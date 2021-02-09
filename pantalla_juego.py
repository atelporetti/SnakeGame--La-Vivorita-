try:
    from tkinter import Frame, Label
except:
    from Tkinter import Frame, Label
import constantes
from vivorita import VivoritaPantalla

class PantallaJuego(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        self.config(background='black', width=constantes.WINDOW_WIDTH, height=constantes.WINDOW_HEIGHT)
        self.grid(row=0, column=0, sticky='nsew')
        self.rowconfigure((0, 2), weight=1)
        self.columnconfigure((0, 1), weight=1)

        self.lb_nombre = Label(self, text=f'Puntaje de {self.master.nombre.get()}', font=(constantes.tipografia, 6, "bold"))
        self.lb_nombre.grid(row=0, column=0, padx=0, pady=0)
        self.lb_nombre.config(bg=constantes.color_fondo, fg='white',
                            justify='left',
                            font=(constantes.tipografia, 12))

        self.lb_nombre = Label(self, textvariable=self.master.puntaje, font=(constantes.tipografia, 6, "bold"))
        self.lb_nombre.grid(row=0, column=1, padx=0, pady=0)
        self.lb_nombre.config(bg=constantes.color_fondo, fg='orange',
                            justify='left',
                            font=(constantes.tipografia, 12))

        self.vivora = VivoritaPantalla(self)
        self.vivora.config(bg=constantes.color_fondo, width=constantes.CANVA_WIDTH,
                    height=constantes.CANVA_HEIGHT, highlightthickness=0)
        self.vivora.grid(row=1, column=0, columnspan=2)