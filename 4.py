import pygame
from tkinter import *
from tkinter import font
import os
import platform
from itertools import cycle
import traceback


class Game(Tk):
    def __init__(self):
        Tk.__init__(self)
        # some SDL magic (don't know how and why this works tbh)
        os.environ['SDL_WINDOWID'] = str(self.winfo_id())
        if platform.system == "Windows":
            os.environ['SDL_VIDEODRIVER'] = 'windib'
        
        # itialize a pygame display
        pygame.init()
        self.screen = pygame.display.set_mode((700, 720))
        self.screen.fill(pygame.Color('red'))
        self.clock = pygame.time.Clock()
        # --------------------------------------------------------------
        # everything from here is optional and only for demonstration

        # create a cycle of colors to have something that animates
        self.timer = 0
        self.colors = cycle(['red', 'yellow', 'green', 'turquoise', 
                             'blue', 'purple'])
        # different delay times in second that one can iterate over
        self.delays = cycle([1, 0.5, 0.1])
        self.color = next(self.colors)
        self.delay = next(self.delays)
        
        # create a tk Button that changes the animation speed
        helv = font.Font(family='Helvetica', size=18, weight='bold')
        self.button = Button(self, 
                                text="Change speed",
                                font=helv,
                                command=self.change_speed).pack(side=BOTTOM)
        # ---------------------------------------------------------------
    
    def change_speed(self):
        # change the animation delay
        self.delay = next(self.delays)
        
    def run(self):
        # Pygame loop
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            self.timer += self.clock.tick(60) / 1000

            # --- also optional ----------------------------
            # change the screen color after the given delay
            if self.timer >= self.delay:
                self.color = next(self.colors)
                self.timer = 0
            self.screen.fill(pygame.Color(self.color))    
            # ----------------------------------------------

            pygame.display.update()
            
            # update the tkinter root (I need this try except for some reason,
            # otherwise I get an error when closing the window)
            try:
                self.update()
            except TclError:
                running = False   
        pygame.quit()

try:
    
    # initialise the root widget
    root = Game()
    ancho_pantalla = root.winfo_screenwidth()
    alto_pantalla = root.winfo_screenheight()
    root.geometry(f'700x720+{str(int(ancho_pantalla-0.75*ancho_pantalla))}+0')
    # initialise and run the game

    root.run()
    
except Exception:
    traceback.print_exc()
    pygame.quit()