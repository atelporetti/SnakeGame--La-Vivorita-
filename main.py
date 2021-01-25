from tkinter import *

from pygame import Color
from ventana_inicio import *
import constantes
pygame.init()

# -------------- CONTANTES---------------
filas = 5
columnas = 2
# --------
if __name__ == "__main__":
    raiz = Tk()
    raiz.title(constantes.titulo)
    raiz.resizable(False, False)
    raiz.iconbitmap(constantes.icon)
    ancho_pantalla = raiz.winfo_screenwidth()
    raiz.geometry(f'723x698+{str(int(ancho_pantalla-0.75*ancho_pantalla))}+0')
    # De permitir que se modifique el tamaño de pantalla, este seria el tamaño maximo permitido
    raiz.maxsize(1366, 698)
    # raiz.state("zoomed")
    raiz.config(bg='black',
                bd='20',
                relief='groove',
                cursor='tcross')
    raiz.rowconfigure((0, filas), weight=1)
    raiz.columnconfigure((0, columnas), weight=1)

    Inicio(raiz).grid(sticky='nsew')

    raiz.mainloop()
