from tkinter import *
import pygame

# El ícono del juego es de: "Snake by José Manuel de Laá from the Noun Project"


pygame.init()

filas = 5
columnas = 2


raiz = Tk()
raiz.title('La Vivorita: el juego')
raiz.resizable(True, True)
raiz.iconbitmap('snake.ico')
# La raiz se adapta al tamaño de su contenedor interno
# raiz.geometry('640x480')
raiz.config(bg='black', width='640', height='480',
            bd='20', relief='groove', cursor='tcross')
raiz.rowconfigure((0, filas), weight=1)
raiz.columnconfigure((0, columnas), weight=1)


# -------------- IMAGEN---------------

imagen_bienvenida = PhotoImage(file='img/snakeWelcomeResized2.png')
# Para ajustar la imagen
imagen_bienvenida = imagen_bienvenida.zoom(1, 1)
imagen_bienvenida = imagen_bienvenida.subsample(1)
# ------------------------------------


frame = Frame(raiz)
frame.config(background='black')  # tcross, cross, dotbox
# Rellena el frame y el fondo de la raiz no se ve
frame.grid(sticky='nsew')
frame.rowconfigure((0, filas), weight=1)
frame.columnconfigure((0, columnas), weight=1)

#MEJORAR EL SCROLL
scroll = Scrollbar(raiz, command=frame)
scroll.grid(row=0, column=3, sticky='nsew') 

lb_bienvenida_img = Label(frame, image=imagen_bienvenida)
lb_bienvenida_img.grid(row=0, column=0, columnspan=2,
                    sticky='nsew', padx=10, pady=10)

lb_bienvenida = Label(frame, text='La Vivorita: el juego',
                   font=("256 Bytes", 40), bg='black', fg='white')
# RitzFLF, 256 Bytes, RightBankFLF, Franchise,
lb_bienvenida.grid(row=1, column=0, columnspan=3, sticky='nsew', padx=10, pady=10)
lb_bienvenida.rowconfigure((0, filas), weight=1)
lb_bienvenida.columnconfigure((0, columnas), weight=1)


nombre = StringVar()

lb_nombre_j = Label(frame, text='Nombre Jugador:')
lb_nombre_j.config(bg='black', fg='white', font=("RitzFLF", 12))
lb_nombre_j.grid(row=2, column=0, sticky='nsew', padx=10, pady=10)
lb_nombre_jugador = Entry(frame, textvariable=nombre)
lb_nombre_jugador.grid(row=2, column=1, sticky='nsew', padx=10, pady=10)
lb_nombre_jugador.config(bg='black', fg='#B2BD08',
                      justify='center', font=("RitzFLF", 12))

msg_alerta = Message(frame)
msg_alerta.grid(row=4, column=0, sticky='nsew', padx=10, pady=10)
msg_alerta.config(bg='black', fg='red', justify='left', anchor=CENTER, font=("RitzFLF", 12))

def msj_alerta(msj):
    msg_alerta.config(text=str(msj))

"""
def play():
    pygame.mixer.music.load('audio\snake.mp3')
    pygame.mixer.music.play()


Button(raiz, text="Play", command=play).grid(
    row=2, column=2, sticky='nsew', padx=10, pady=10)


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

txt_musica_on_off = 'Musica OFF'


def cambio_musica():
    if btn_musica_on_off['text'] == 'Musica OFF':
        btn_musica_on_off['text'] = 'Musica ON'
        btn_musica_on_off['fg'] = '#B2BD08'
        pygame.mixer.music.pause()
    elif btn_musica_on_off['text'] == 'Musica ON':
        btn_musica_on_off['text'] = 'Musica OFF'
        btn_musica_on_off['fg'] = 'white'
        pygame.mixer.music.unpause()


btn_musica_on_off = Button(
    frame, text=txt_musica_on_off, command=cambio_musica)

btn_musica_on_off.grid(row=4, column=1, sticky='nsew', padx=10, pady=10)
btn_musica_on_off.config(bg='black', fg='white',
                         justify='center', font=("RitzFLF", 12))


velocidad = 0
dificultad = IntVar()

def cambia_dificultad():
    if dificultad.get() == 1:
        velocidad = 1
        rb_facil['fg'] = '#B2BD08'
        rb_dificil['fg'] = 'white'
    elif dificultad.get() == 2:
        velocidad = 2
        rb_dificil['fg'] = '#B2BD08'
        rb_facil['fg'] = 'white'

def guarda_datos():
    alerta = ''
    if (nombre.get() == '' and dificultad.get() == 0):
        alerta = 'Elija un nombre y nivel de dificultad'
        msj_alerta(alerta)
        return print(alerta)
    if (nombre.get() == ''):
        alerta = 'Elija un nombre'
        msj_alerta(alerta)
        return print(alerta)
    if (dificultad.get() == 0):
        alerta = 'Elija la dificultad'
        msj_alerta(alerta)
        return print(alerta)
    elif (nombre.get() and dificultad.get()):
        print('Comenzando juego...')
        msj_alerta(alerta)
        return nombre.get(), dificultad.get()


rb_facil = Radiobutton(frame, text='Fácil', variable=dificultad, value=1, command=cambia_dificultad)
rb_facil.config(bg='black', fg='white', justify='center', font=("RitzFLF", 12))
rb_facil.grid(row=3, column=0, sticky='nsew', padx=10, pady=10)
rb_dificil = Radiobutton(frame, text='Dificil', variable=dificultad, value=2, command=cambia_dificultad)
rb_dificil.config(bg='black', fg='white', justify='center', font=("RitzFLF", 12))
rb_dificil.grid(row=3, column=1, sticky='nsew', padx=10, pady=10)

btn_jugar = Button(frame, text='JUGAR')
btn_jugar.grid(row=5, column=0, columnspan=2, sticky='nsew', padx=10, pady=10)
btn_jugar.config(bg='black', fg='#B2BD08', justify='center',
             font=("256 Bytes", 20), command=guarda_datos)
btn_jugar.rowconfigure((0, filas), weight=1)
btn_jugar.columnconfigure((0, columnas), weight=1)


raiz.mainloop()
