from tkinter import *

master = Tk()

class Vivorita():
    def __init__(self, raiz):
        self.raiz = raiz
        x, y = utils.random_coordinates()
        self.blocks = collections.deque([shapes.Block(raiz, x, y)])
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