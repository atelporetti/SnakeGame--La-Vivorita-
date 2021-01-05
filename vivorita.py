from tkinter import *
import pygame

# El ícono del juego es de: "Snake by José Manuel de Laá from the Noun Project"


pygame.init()

raiz = Tk()
raiz.title('La Vivorita: el juego')
raiz.resizable(True, True)
raiz.iconbitmap('snake.ico')
# La raiz se adapta al tamaño de su contenedor interno
# raiz.geometry('640x480')
raiz.config(bg='black', width='640', height='480',
            bd='20', relief='groove', cursor='tcross')
raiz.rowconfigure((0,3), weight=1)
raiz.columnconfigure((0,1), weight=1)

imagen_bienvenida = PhotoImage(file='img/snakeWelcomeResized.png')
# Para ajustar la imagen
imagen_bienvenida = imagen_bienvenida.zoom(1, 1)
imagen_bienvenida = imagen_bienvenida.subsample(1)

frame = Frame(raiz)
frame.config(background='black')  # tcross, cross, dotbox
# Rellena el frame y el fondo de la raiz no se ve
frame.grid(sticky='nsew')
frame.rowconfigure((0,3), weight=1)
frame.columnconfigure((0,1), weight=1)


bienvenida_img = Label(frame, image=imagen_bienvenida)
bienvenida_img.grid(row=0, column=0, columnspan=2,
                    sticky='nsew', padx=10, pady=10)
bienvenida_img.rowconfigure((0,3), weight=1)
bienvenida_img.columnconfigure((0,1), weight=1)

bienvenida = Label(frame, text='La Vivorita: el juego', font=("256 Bytes", 40), bg='black', fg='white')
# RitzFLF, 256 Bytes, RightBankFLF, Franchise,
bienvenida.grid(row=1, column=0, columnspan=2, sticky='nsew', padx=10, pady=10)
bienvenida.rowconfigure((0,3), weight=1)
bienvenida.columnconfigure((0,1), weight=1)

nombre_j = Label(frame, text='Nombre Jugador:')
nombre_j.config(bg='black', fg='white', font=("RitzFLF", 12))
nombre_j.grid(row=2, column=0, sticky='nsew', padx=10, pady=10)
nombre_jugador = Entry(frame)
nombre_jugador.grid(row=2, column=1, sticky='nsew', padx=10, pady=10)
nombre_jugador.config(bg='black', fg='#B2BD08', justify='center', font=("RitzFLF", 12))

txt_musica_on_off = 'Musica OFF'

def play():
    pygame.mixer.music.load('snake.mp3') #Loading File Into Mixer
    pygame.mixer.music.play() #Playing It In The Whole Device
Button(raiz,text="Play",command=play).grid(row=2, column=2, sticky='nsew', padx=10, pady=10)

"""
Background Music:
0:00 - Main Menu
0:18 - Gameplay

Sound Effects:
0:31 - Victory
0:35 - Game Over
0:39 - Select (menu)
0:40 - Fruit
0:41 - Fail
0:43 - Bomb
0:46 - Power Up
"""

def cambio_musica():
    if btn_musica_on_off['text'] == 'Musica OFF':
        btn_musica_on_off['text'] = 'Musica ON'
        btn_musica_on_off['fg'] = '#B2BD08'
    elif btn_musica_on_off['text'] == 'Musica ON':
        btn_musica_on_off['text'] = 'Musica OFF'
        btn_musica_on_off['fg'] = 'white'
        pygame.mixer.music.load('audio/snake.mp3')
        pygame.mixer.music.play()

btn_musica_on_off = Button(
    frame, text=txt_musica_on_off, command=cambio_musica)

btn_musica_on_off.grid(row=3, column=1, sticky='nsew', padx=10, pady=10)
btn_musica_on_off.config(bg='black', fg='white', justify='center', font=("RitzFLF", 12))
raiz.mainloop()
