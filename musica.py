import pygame

class Reproductor():
    pygame.mixer.pre_init(44100, -16, 2, 2048)
    pygame.mixer.init()
    
    def __init__(self):
        pygame.mixer.pre_init(44100, -16, 2, 2048)
        pygame.mixer.init()

    def reproducir_musica(self, tema, volumen):
        pygame.mixer.music.load(tema)
        pygame.mixer.music.set_volume(volumen)
        pygame.mixer.music.play(-1)
    
    def reproducir_sonido(self, tema, volumen):
        self.sonido = pygame.mixer.Sound(tema)
        self.sonido.set_volume(volumen)
        pygame.mixer.Sound.play(self.sonido)

    def para_sonido(self):
        pygame.mixer.music.stop()
    
    def pausa_sonido(self):
        pygame.mixer.music.pause()
    
    def reanuda_sonido(self):
        pygame.mixer.music.unpause()