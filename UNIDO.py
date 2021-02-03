try:
    from tkinter import *
except:
    from Tkinter import *
import pygame
from threading import *
import constantes

# El ícono del juego es de: "Snake by José Manuel de Laá from the Noun Project"
# La tipografia “8-bit pusab” creada por Seba Perez proviene de https://www.dafont.com/es/8-bit-pusab.font

pygame.init()
raiz = Tk()

# -------------- CONTANTES---------------
filas = 5
columnas = 2
# ---------------------------------------

# -------------- VARIABLES---------------
nombre = StringVar()
velocidad = IntVar()
dificultad = IntVar()
ancho_pantalla = raiz.winfo_screenwidth()
alto_pantalla = raiz.winfo_screenheight()
# ---------------------------------------


raiz.title(constantes.titulo)
raiz.resizable(False, False)
raiz.iconbitmap(constantes.icon)
raiz.geometry(f'723x700+{str(int(ancho_pantalla-0.75*ancho_pantalla))}+0')
# De permitir que se modifique el tamaño de pantalla, este seria el tamaño maximo permitido
#raiz.maxsize(1366, 700)
# raiz.state("zoomed")
raiz.config(bg='black',
            bd='20',
            relief='groove',
            cursor='tcross')
raiz.rowconfigure((0, filas), weight=1)
raiz.columnconfigure((0, columnas), weight=1)
#raiz.call("tk", "scaling", 1.0)
# -------------- IMAGEN---------------
ph_imagen_bienvenida = PhotoImage(file=constantes.imagen_fondo)
# Para ajustar la imagen
#ph_imagen_bienvenida = ph_imagen_bienvenida.zoom(1, 1)
#ph_imagen_bienvenida = ph_imagen_bienvenida.subsample(1)
# ------------------------------------

frame = Frame(raiz)
frame.config(background='black')  # tcross, cross, dotbox
frame.grid(row=0, column=0)
#frame.rowconfigure((0, filas), weight=1)
#frame.columnconfigure((0, columnas), weight=1)

# -------------- SCROLL---------------
#scroll = Scrollbar(raiz, command=frame)
#scroll.grid(row=0, column=3, sticky='nsew')
# ------------------------------------

lb_bienvenida_img = Label(frame, image=ph_imagen_bienvenida, bg='black')
lb_bienvenida_img.grid(row=0, column=0, columnspan=2,
                       sticky='nsew',
                       padx=10, pady=10)

lb_bienvenida = Label(frame, text=constantes.titulo,
                      font=(constantes.tipografia, 20),
                      bg='black',
                      fg='white')
# 8-bit pusab, 256 Bytes, RightBankFLF, Franchise, 8-bit pusab, Connection
lb_bienvenida.grid(row=1, column=0, columnspan=3,
                   sticky='nsew',
                   padx=10, pady=10)
#lb_bienvenida.rowconfigure((0, filas), weight=1)
#lb_bienvenida.columnconfigure((0, columnas), weight=1)


lb_nombre_j = Label(frame, text='Nombre Jugador:')
lb_nombre_j.config(bg='black', fg='white', font=(constantes.tipografia, 12))
lb_nombre_j.grid(row=2, column=0, sticky='nsew', padx=10, pady=10)
lb_nombre_jugador = Entry(frame, textvariable=nombre)
lb_nombre_jugador.grid(row=2, column=1, sticky='nsew', padx=10, pady=10)
lb_nombre_jugador.config(bg='black', fg='#B2BD08',
                         justify='center', font=(constantes.tipografia, 12))
lb_nombre_jugador.focus()

msg_alerta = Label(frame)
msg_alerta.grid(row=4, column=0, sticky='nsew', padx=10, pady=10)
msg_alerta.config(bg='black', fg='red', justify='left',
                  anchor=CENTER, font=(constantes.tipografia, 12))


def msj_alerta(msj):
    msg_alerta.config(text=str(msj))


# -------------- MUSICA---------------
#sound_effect = pygame.mixer.Sound('audio/snake.wav') 
#pygame.mixer.Sound.play(sound_effect)
#pygame.mixer.music.load('audio/inicio.wav')
#pygame.mixer.music.play(-1)
# ------------------------------------

txt_musica_on_off = 'Musica OFF'


def cambio_musica():
    if btn_musica_on_off['text'] == 'Musica OFF':
        btn_musica_on_off['text'] = 'Musica ON'
        btn_musica_on_off['fg'] = '#B2BD08'
        #pygame.mixer.music.pause()
    elif btn_musica_on_off['text'] == 'Musica ON':
        btn_musica_on_off['text'] = 'Musica OFF'
        btn_musica_on_off['fg'] = 'white'
        #pygame.mixer.music.unpause()


btn_musica_on_off = Button(
    frame, text=txt_musica_on_off, command=cambio_musica)

btn_musica_on_off.grid(row=4, column=1, sticky='nsew', padx=10, pady=10)
btn_musica_on_off.config(bg='black', fg='white',
                         justify='center', font=(constantes.tipografia, 12))


def cambia_dificultad():
    if dificultad.get() == 1:
        velocidad = 1
        rb_facil['fg'] = '#B2BD08'
        rb_dificil['fg'] = 'white'
    elif dificultad.get() == 2:
        velocidad = 2
        rb_dificil['fg'] = '#B2BD08'
        rb_facil['fg'] = 'white'


def borrar_widget_grid():
    frame.grid_remove()
    otro_frame.grid(row=0, column=0)
    # frame.destroy()
    print("Ventana Inicio borrada")


def guarda_datos():
    alerta = ''
    if (nombre.get() == '' and dificultad.get() == 0):
        alerta = 'Elija un nombre \nElija dificultad'
        msj_alerta(alerta)
        return print(alerta)
    elif (nombre.get() == ''):
        alerta = 'Elija un nombre'
        msj_alerta(alerta)
        return print(alerta)
    elif (dificultad.get() == 0):
        alerta = 'Elija la dificultad'
        msj_alerta(alerta)
        return print(alerta)
    elif (nombre.get() and dificultad.get()):
        alerta = 'Comenzando...'
        msj_alerta(alerta)
        t = Timer(1.0, borrar_widget_grid)
        t.start()
        pygame.mixer.music.stop()
        sound_effect = pygame.mixer.Sound('audio/power_up.wav') 
        pygame.mixer.Sound.play(sound_effect)
        return nombre.get(), dificultad.get()


rb_facil = Radiobutton(frame,
                       text='Facil',
                       variable=dificultad,
                       value=1,
                       command=cambia_dificultad)
rb_facil.config(bg='black', fg='white', justify='center',
                font=(constantes.tipografia, 12))
rb_facil.grid(row=3, column=0, sticky='nsew', padx=10, pady=10)
rb_dificil = Radiobutton(frame,
                         text='Dificil',
                         variable=dificultad,
                         value=2,
                         command=cambia_dificultad)
rb_dificil.config(bg='black', fg='white',
                  justify='center', font=(constantes.tipografia, 12))
rb_dificil.grid(row=3, column=1, sticky='nsew', padx=10, pady=10)

btn_jugar = Button(frame, text='JUGAR')
btn_jugar.grid(row=5, column=0, columnspan=2, sticky='nsew', padx=10, pady=10)
btn_jugar.config(bg='black',
                 fg='#B2BD08',
                 justify='center',
                 font=(constantes.tipografia, 12),
                 command=lambda: [guarda_datos()])
#btn_jugar.rowconfigure((0, filas), weight=1)
#btn_jugar.columnconfigure((0, columnas), weight=1)

otro_frame = Canvas(raiz)
otro_frame.config(bg='red', width=723, height=700)

lb_nombre_j = Label(otro_frame, text='Nombre Jugador:')
lb_nombre_j.config(bg='black', fg='white', font=(constantes.tipografia, 12))
lb_nombre_j.grid(row=2, column=0, sticky='nsew', padx=10, pady=10)
lb_nombre_jugador = Entry(otro_frame, textvariable=nombre)
lb_nombre_jugador.grid(row=2, column=1, sticky='nsew', padx=10, pady=10)
lb_nombre_jugador.config(bg='black', fg='#B2BD08',
                         justify='center', font=(constantes.tipografia, 12))
lb_nombre_jugador.focus()

msg_alerta = Label(otro_frame)
msg_alerta.grid(row=4, column=0, sticky='nsew', padx=10, pady=10)
msg_alerta.config(bg='black', fg='red', justify='left',
                  anchor=CENTER, font=(constantes.tipografia, 12))


raiz.mainloop()
