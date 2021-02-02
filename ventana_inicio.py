try:
    from tkinter import *
except:
    from Tkinter import *
import constantes, pygame, os, platform
from threading import Timer

class Inicio(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.master = master
        self._frame = Frame(master)
        self._frame.config(bg=constantes.color_fondo)
        self._frame.grid(row=0, column=0)
        self.config(background=constantes.color_fondo)
        self.grid(sticky='nsew')
        self.rowconfigure((0, constantes.filas), weight=1)
        self.columnconfigure((0, constantes.columnas), weight=1)

        self.nombre = StringVar()
        self.velocidad = IntVar()
        self.dificultad = IntVar()

        self.reproducir_musica()
        self.crear_widgets()

    def crear_widgets(self):
        self.ph_imagen_bienvenida = PhotoImage(file=constantes.imagen_fondo)
        self.lb_bienvenida_img = Label(self._frame, image=self.ph_imagen_bienvenida, bg=constantes.color_fondo)
        self.lb_bienvenida_img.grid(row=0, column=0, columnspan=2,
                                    sticky='nsew',
                                    padx=10, pady=10)

        self.lb_bienvenida = Label(self._frame, text=constantes.titulo,
                                    font=(constantes.tipografia, 20),
                                    bg=constantes.color_fondo,
                                    fg='white')
        self.lb_bienvenida.grid(row=1, column=0, columnspan=3,
                                sticky='nsew',
                                padx=10, pady=10)              

        self.lb_nombre_j = Label(self._frame, text='Nombre Jugador:')
        self.lb_nombre_j.config(bg=constantes.color_fondo,
                                fg='white',
                                font=(constantes.tipografia, 12))
        self.lb_nombre_j.grid(row=2, column=0, sticky='nsew', padx=10, pady=10)

        self.lb_nombre_jugador = Entry(self._frame, textvariable=self.nombre)
        self.lb_nombre_jugador.grid(row=2, column=1, sticky='nsew', padx=10, pady=10)
        self.lb_nombre_jugador.config(bg=constantes.color_fondo, fg=constantes.color_tipografia,
                                justify='center', font=(constantes.tipografia, 12))
        self.lb_nombre_jugador.focus()

        self.msg_alerta = Label(self._frame)
        self.msg_alerta.grid(row=4, column=0, sticky='nsew', padx=10, pady=10)
        self.msg_alerta.config(bg=constantes.color_fondo,
                                fg='red',
                                justify='left',
                                anchor=CENTER,
                                font=(constantes.tipografia, 12))

        self.txt_musica_on_off = 'Musica OFF'
        self.btn_musica_on_off = Button(self._frame, text=self.txt_musica_on_off, command=self.cambio_musica)
        self.btn_musica_on_off.grid(row=4, column=1, sticky='nsew', padx=10, pady=10)
        self.btn_musica_on_off.config(bg=constantes.color_fondo, fg='white',
                                        justify='center',
                                        font=(constantes.tipografia, 12))

        self.rb_facil = Radiobutton(self._frame,
                            text='Facil',
                            variable=self.dificultad,
                            value=1,
                            command=self.cambia_dificultad)
        self.rb_facil.config(bg=constantes.color_fondo, fg='white',
                            justify='center',
                            font=(constantes.tipografia, 12))
        self.rb_facil.grid(row=3, column=0, sticky='nsew', padx=10, pady=10)

        self.rb_dificil = Radiobutton(self._frame,
                                text='Dificil',
                                variable=self.dificultad,
                                value=2,
                                command=self.cambia_dificultad)
        self.rb_dificil.config(bg=constantes.color_fondo, fg='white',
                        justify='center', font=(constantes.tipografia, 12))
        self.rb_dificil.grid(row=3, column=1, sticky='nsew', padx=10, pady=10)

        self.btn_jugar = Button(self._frame, text='JUGAR')
        self.btn_jugar.grid(row=5, column=0, columnspan=2, sticky='nsew', padx=10, pady=10)
        self.btn_jugar.config(bg=constantes.color_fondo,
                        fg=constantes.color_tipografia,
                        justify='center',
                        font=(constantes.tipografia, 12),
                        command=lambda:[self.guarda_datos()])
    
    def reproducir_musica(self):
        pygame.mixer.pre_init(44100, -16, 2, 2048)
        pygame.mixer.init()
        pygame.mixer.music.load(constantes.musica_inicio)
        pygame.mixer.music.set_volume(0.4)
        pygame.mixer.music.play(-1)

    def msj_alerta(self, msj):
        self.msg_alerta.config(text=str(msj))
        
    def cambio_musica(self):
        if self.btn_musica_on_off['text'] == 'Musica OFF':
            self.btn_musica_on_off['text'] = 'Musica ON'
            self.btn_musica_on_off['fg'] = constantes.color_tipografia
            pygame.mixer.music.pause()
        elif self.btn_musica_on_off['text'] == 'Musica ON':
            self.btn_musica_on_off['text'] = 'Musica OFF'
            self.btn_musica_on_off['fg'] = 'white'
            pygame.mixer.music.unpause()
        
    def cambia_dificultad(self):
        if self.dificultad.get() == 1:
            self.velocidad = 1
            self.rb_facil['fg'] = constantes.color_tipografia
            self.rb_dificil['fg'] = 'white'
        elif self.dificultad.get() == 2:
            self.velocidad = 2
            self.rb_dificil['fg'] = constantes.color_tipografia
            self.rb_facil['fg'] = 'white'
    
    def guarda_datos(self):
        alerta = ''
        if (self.nombre.get() == '' and self.dificultad.get() == 0):
            alerta = 'Elija un nombre \nElija dificultad'
            self.msj_alerta(alerta)
        elif (self.nombre.get() == ''):
            alerta = 'Elija un nombre'
            self.msj_alerta(alerta)
        elif (self.dificultad.get() == 0):
            alerta = 'Elija la dificultad'
            self.msj_alerta(alerta)
        elif (self.nombre.get() and self.dificultad.get()):
            alerta = 'Comenzando...'
            self.msj_alerta(alerta)
            t = Timer(1.5, lambda:[self.borrar_widget_grid()])
            t.start()
            pygame.mixer.music.stop()
            sound_effect = pygame.mixer.Sound(constantes.musica_play)
            sound_effect.set_volume(0.5)
            pygame.mixer.Sound.play(sound_effect)
            return self.nombre.get(), self.dificultad.get()

    def borrar_widget_grid(self):
        self._frame.grid_remove()
        from pantalla_juego import PantallaJuego
        self.master.cambia_frame(PantallaJuego, self.master)
    
    def invisibilizar(self):
        self.master.withdraw()    