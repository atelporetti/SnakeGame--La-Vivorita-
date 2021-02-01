try:
    from tkinter import *
except:
    from Tkinter import *
import os, pygame, platform, traceback
from ventana_inicio import Inicio
from pantalla_juego import PantallaJuego
import constantes

class Main(Tk):
    def __init__(self):
        Tk.__init__(self)
        self._frame = None
        #self.cambia_frame(Inicio)
        self.title(constantes.titulo)
        self.resizable(False, False)
        self.iconbitmap(constantes.icon)
        self.ancho_pantalla = self.winfo_screenwidth()
        self.alto_pantalla = self.winfo_screenheight()
        self.geometry(
            f'{str(constantes.WINDOW_WIDTH)}x{str(constantes.WINDOW_HEIGHT)}+{str(int(self.ancho_pantalla-0.75*self.ancho_pantalla))}+0')
        # De permitir que se modifique el tamaño de pantalla, este seria el tamaño maximo permitido
        self.maxsize(1366, 700)
        # raiz.state("zoomed")
        self.config(bg='black',
                    bd='20',
                    relief='groove',
                    cursor='tcross')
        self.rowconfigure((0, constantes.filas), weight=1)
        self.columnconfigure((0, constantes.columnas), weight=1)

    def cambia_frame(self, frame_a_cambiar):
        nuevo_frame = frame_a_cambiar(self)
        if self._frame is not None:
            self._frame.grid_remove()
        self._frame = nuevo_frame
        self._frame.grid(row=0, column=0)

try:
    if __name__ == "__main__":
        root = Main()
        root.overrideredirect(False)  # deshace el marco
        Inicio(root)
        root.mainloop()
except:
    traceback.print_exc()
    pygame.quit()