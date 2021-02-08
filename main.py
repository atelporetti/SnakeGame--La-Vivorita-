try:
    from tkinter import *
except:
    from Tkinter import *
import time
import traceback
import constantes
from ventana_inicio import Inicio


class Main(Tk):

    def __init__(self):
        Tk.__init__(self)
        self._frame = None
        self.title(constantes.titulo)
        self.resizable(False, False)
        self.iconbitmap(constantes.icon)
        self.ancho_pantalla = self.winfo_screenwidth()
        self.alto_pantalla = self.winfo_screenheight()
        self.geometry(
            f'{str(constantes.WINDOW_WIDTH)}x{str(constantes.WINDOW_HEIGHT)}+{str(int(self.ancho_pantalla-0.75*self.ancho_pantalla))}+0')
        self.config(bg='black',
                    bd='20',
                    relief='groove',
                    cursor='tcross')
        self.call("tk", "scaling", 1)
        self.overrideredirect(False)  # deshace el marco
        self.rowconfigure((0, 1), weight=0)
        self.columnconfigure((0, 1), weight=0)

        self.puntaje = IntVar()
        self.nombre = StringVar()
        self.dificultad = IntVar()
        self.velocidad = IntVar()
        self.tiempo = time.time()

    def cambia_frame(self, frame_a_cambiar, master):
        nuevo_frame = frame_a_cambiar(master)
        if self._frame is not None:  # si no es la primera vez que inicia el programa
            self._frame.grid_remove()
        self._frame = nuevo_frame
        self._frame.grid(row=0, column=0)


try:
    if __name__ == "__main__":
        root = Main()
        root.cambia_frame(Inicio, root)
        #root.cambia_frame(PantallaJuego, root)
        root.mainloop()
except:
    traceback.print_exc()
