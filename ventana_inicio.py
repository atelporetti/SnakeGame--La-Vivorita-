from threading import Timer
from tkinter import *
import constantes
import pygame
import main

class Inicio(Frame):
    def __init__(self, padre, *args, **kwargs):
        super().__init__(padre, *args, **kwargs)
        self.padre = padre
        self.config(background='black')  # tcross, cross, dotbox
        self.grid(sticky='nsew')
        self.rowconfigure((0, main.filas), weight=1)
        self.columnconfigure((0, main.columnas), weight=1)

        self.nombre = StringVar()
        self.velocidad = IntVar()
        self.dificultad = IntVar()

        self.crear_widgets()

    def crear_widgets(self):

        self.ph_imagen_bienvenida = PhotoImage(file=constantes.imagen_fondo)
        self.lb_bienvenida_img = Label(self.padre, image=self.ph_imagen_bienvenida, bg='black')
        self.lb_bienvenida_img.grid(row=0, column=0, columnspan=2,
                                    sticky='nsew',
                                    padx=10, pady=10)

        self.lb_bienvenida = Label(self.padre, text=constantes.titulo,
                        # RitzFLF, 256 Bytes, RightBankFLF, Franchise,
                                    font=(constantes.tipografia, 20),
                                    bg='black',
                                    fg='white')
        self.lb_bienvenida.grid(row=1, column=0, columnspan=3,
                                sticky='nsew',
                                padx=10, pady=10)              

        self.lb_nombre_j = Label(self.padre, text='Nombre Jugador:')
        self.lb_nombre_j.config(bg='black',
                                fg='white',
                                font=(constantes.tipografia, 12))
        self.lb_nombre_j.grid(row=2, column=0, sticky='nsew', padx=10, pady=10)

        self.lb_nombre_jugador = Entry(self.padre, textvariable=self.nombre)
        self.lb_nombre_jugador.grid(row=2, column=1, sticky='nsew', padx=10, pady=10)
        self.lb_nombre_jugador.config(bg='black', fg='#B2BD08',
                                justify='center', font=(constantes.tipografia, 12))

        self.msg_alerta = Label(self.padre)
        self.msg_alerta.grid(row=4, column=0, sticky='nsew', padx=10, pady=10)
        self.msg_alerta.config(bg='black',
                                fg='red',
                                justify='left',
                                anchor=CENTER,
                                font=(constantes.tipografia, 12))

        self.txt_musica_on_off = 'Musica OFF'
        self.btn_musica_on_off = Button(self.padre, text=self.txt_musica_on_off, command=self.cambio_musica)
        self.btn_musica_on_off.grid(row=4, column=1, sticky='nsew', padx=10, pady=10)
        self.btn_musica_on_off.config(bg='black', fg='white',
                                        justify='center',
                                        font=(constantes.tipografia, 12))

        self.rb_facil = Radiobutton(self.padre,
                            text='Facil',
                            variable=self.dificultad,
                            value=1,
                            command=self.cambia_dificultad)
        self.rb_facil.config(bg='black', fg='white',
                            justify='center',
                            font=(constantes.tipografia, 12))
        self.rb_facil.grid(row=3, column=0, sticky='nsew', padx=10, pady=10)

        self.rb_dificil = Radiobutton(self.padre,
                                text='Dificil',
                                variable=self.dificultad,
                                value=2,
                                command=self.cambia_dificultad)
        self.rb_dificil.config(bg='black', fg='white',
                        justify='center', font=(constantes.tipografia, 12))
        self.rb_dificil.grid(row=3, column=1, sticky='nsew', padx=10, pady=10)

        self.btn_jugar = Button(self.padre, text='JUGAR')
        self.btn_jugar.grid(row=5, column=0, columnspan=2, sticky='nsew', padx=10, pady=10)
        self.btn_jugar.config(bg='black',
                        fg='#B2BD08',
                        justify='center',
                        font=(constantes.tipografia, 20),
                        command=lambda:[self.guarda_datos()])
        
    def msj_alerta(self, msj):
        self.msg_alerta.config(text=str(msj))
        
    def cambio_musica(self):
        if self.btn_musica_on_off['text'] == 'Musica OFF':
            self.btn_musica_on_off['text'] = 'Musica ON'
            self.btn_musica_on_off['fg'] = '#B2BD08'
            pygame.mixer.music.pause()
        elif self.btn_musica_on_off['text'] == 'Musica ON':
            self.btn_musica_on_off['text'] = 'Musica OFF'
            self.btn_musica_on_off['fg'] = 'white'
            pygame.mixer.music.unpause()
    """
    def play(self):
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
        
    def guarda_datos(self):
        alerta = ''
        if (self.nombre.get() == '' and self.dificultad.get() == 0):
            alerta = 'Elija un nombre \nElija dificultad'
            self.msj_alerta(alerta)
            return print(alerta)
        elif (self.nombre.get() == ''):
            alerta = 'Elija un nombre'
            self.msj_alerta(alerta)
            return print(alerta)
        elif (self.dificultad.get() == 0):
            alerta = 'Elija la dificultad'
            self.msj_alerta(alerta)
            return print(alerta)
        elif (self.nombre.get() and self.dificultad.get()):
            alerta = 'Comenzando...'
            self.msj_alerta(alerta)
            t = Timer(2.5, self.borrar_widget_grid)
            t.start()
            return self.nombre.get(), self.dificultad.get()

    def cambia_dificultad(self):
        if self.dificultad.get() == 1:
            velocidad = 1
            self.rb_facil['fg'] = '#B2BD08'
            self.rb_dificil['fg'] = 'white'
        elif self.dificultad.get() == 2:
            velocidad = 2
            self.rb_dificil['fg'] = '#B2BD08'
            self.rb_facil['fg'] = 'white'

    def borrar_widget_grid(self):
        self.grid_forget()
        self.destroy()
        print("Ventana Inicio borrada")

        self.menu = Menu(self.padre)
        self.menu_lista = Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Crear",menu=self.menu_lista)
        self.menu_lista.add_command(label="Crear frame",
                                    command=self.crear_frame
                                    )
        self.menu_notas = Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Borrar", menu=self.menu_notas)
        self.menu_notas.add_command(label="Borrar frame",
                                    command=self.borrar_frame
                                    )
        #padre.config(menu=self.menu)
        #self._frame = None

    def crear_frame(self):
        if self._frame is None:
            self._frame = MyFrame(self)

    def borrar_frame(self):
        if self._frame is not None:
            self._frame.borrar()
            self._frame = None
            
class MyFrame(Frame):
    def __init__(self, padre):
        super().__init__(padre)
        self.pack(fill=BOTH, expand=YES)
        self.config(bg="blue")
        print("Frame creado")

    def borrar(self):
        self.pack_forget()
        self.destroy()
        print("Frame borrado")
