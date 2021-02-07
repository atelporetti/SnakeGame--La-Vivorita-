import pygame

class Reproductor():
    pygame.mixer.pre_init(44100, -16, 2, 2048)
    pygame.mixer.init()
    
    def __init__(self):
        pygame.mixer.pre_init(44100, -16, 2, 2048)
        pygame.mixer.init()

    def reproducir_musica(self, tema, volumen):
        pygame.mixer.music.load(tema) #constantes.musica_en_juego
        pygame.mixer.music.set_volume(volumen) #0.04
        pygame.mixer.music.play(-1)
    
    def reproducir_sonido(self, tema, volumen):
        self.sound_effect = pygame.mixer.Sound(tema) #constantes.musica_comida
        self.sound_effect.set_volume(volumen)
        pygame.mixer.Sound.play(self.sound_effect)

    def para_sonido(self):
        pygame.mixer.music.stop()