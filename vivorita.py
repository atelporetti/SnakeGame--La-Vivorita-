from tkinter import *
from main import Main
master = Tk()

class Vivorita():
    def __init__(self, master):
        self.master = master
        self.cabeza_X = Main.ancho_pantalla
        self.cabeza_Y = Main.alto_pantalla
        self.velocidad_X = 1
        self.velocidad_Y = 1
        self.col
        self.blocks = collections.deque([shapes.Block(master, x, y)])
        self.block_coords = set([(x, y)])

canvas_width = 80
canvas_height = 40
w = Canvas(master, 
           width=canvas_width,
           height=canvas_height)
w.pack()

y = int(canvas_height / 2)
w.create_line(0, y, canvas_width, y, fill="#476042")


mainloop()