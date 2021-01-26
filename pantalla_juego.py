try:
    from tkinter import *
except:
    from Tkinter import *
from ventana_inicio import Inicio


class PantallaJuego(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        Frame.configure(self,bg='blue')
        Label(self, text="Page one", font=('Helvetica', 18, "bold")).grid(row=0, column=0, padx=10, pady=10)

        Button(self, text="Volver a jugar",command=lambda: master.cambia_frame(Inicio)).grid(row=0, column=1, padx=10, pady=10)
