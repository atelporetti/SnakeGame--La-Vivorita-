from ventana_inicio import Inicio
import pandas as pd
import constantes
try:
    from tkinter import Frame, Button, Tk, Label
except:
    from Tkinter import Frame, Button


class Ranking():
    def __init__(self, puntaje, jugador, nivel, tiempo, ubicacion_archivo):
        self.puntaje = puntaje
        self.jugador = jugador
        self.nivel = nivel
        self.tiempo = tiempo
        self.ubicacion_archivo = ubicacion_archivo

    def ordena_puntaje_cvs(self):
        ranking = pd.read_csv(self.ubicacion_archivo, sep=',')
        ranking = ranking.drop_duplicates()
        ranking = ranking.sort_values(['Puntaje'], ascending=False)
        ranking.to_csv(self.ubicacion_archivo, index=False)

    def guarda_partida_csv(self):
        ranking = pd.read_csv(self.ubicacion_archivo, sep=',')
        datos = {
            'Puntaje': [self.puntaje],
            'Jugador': [self.jugador],
            'Nivel': [self.nivel],
            'Tiempo': [self.tiempo]
        }
        data_frame = pd.DataFrame.from_dict(datos)
        ranking = ranking.append(data_frame, sort=False)
        ranking.to_csv(self.ubicacion_archivo, index=False)

    def es_puntaje_alto(self):
        ranking = pd.read_csv(self.ubicacion_archivo, sep=',')
        return self.puntaje > ranking['Puntaje'].max()

    def lee_n_lineas(numero):
        ranking = pd.read_csv(constantes.RANKING, nrows=numero,
                              sep=',', skiprows=1, names=constantes.NOMBRES_COLUMNAS)
        return ranking.values.tolist()


class PantallaRanking(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        #self._frame = Frame(master)
        self.config(background='black', width=constantes.WINDOW_WIDTH,
                    height=constantes.WINDOW_HEIGHT)
        self.grid(row=0, column=0, sticky='nsew')
        self.rowconfigure((0, 2), weight=1)
        self.columnconfigure((0, 1), weight=1)

        self.lb_titulo_puntaje = Label(self, text='Puntajes',
                                        font=(constantes.tipografia, 12),
                                        bg=constantes.color_fondo,
                                        fg='white')
        self.lb_titulo_puntaje.grid(row=0, column=0,
                                    sticky='nsew',
                                    padx=10, pady=10)
        self.lb_titulo_jugador = Label(self, text='Jugador',
                                        font=(constantes.tipografia, 12),
                                        bg=constantes.color_fondo,
                                        fg='white')
        self.lb_titulo_jugador.grid(row=0, column=1,
                                    sticky='nsew',
                                    padx=10, pady=10)
        self.lb_titulo_jugador = Label(self, text='Tiempo de juego (seg)',
                                        font=(constantes.tipografia, 12),
                                        bg=constantes.color_fondo,
                                        fg='white')
        self.lb_titulo_jugador.grid(row=0, column=2,
                                    sticky='nsew',
                                    padx=10, pady=10)

        self.puntajes = Ranking.lee_n_lineas(10)
        row = 1
        for puntaje in self.puntajes:

            self.lb_puntaje = Label(self, text=puntaje[0],
                                    font=(constantes.tipografia, 12),
                                    bg=constantes.color_fondo,
                                    fg='white')
            self.lb_puntaje.grid(row=row, column=0,
                                    sticky='nsew',
                                    padx=10, pady=5)
            self.lb_jugador = Label(self, text=puntaje[1],
                                    font=(constantes.tipografia, 12),
                                    bg=constantes.color_fondo,
                                    fg='white')
            self.lb_jugador.grid(row=row, column=1,
                                    sticky='nsew',
                                    padx=10, pady=5)
            self.lb_nivel = Label(self, text=puntaje[3],
                                    font=(constantes.tipografia, 12),
                                    bg=constantes.color_fondo,
                                    fg='white')
            self.lb_nivel.grid(row=row, column=2,
                                sticky='nsew',
                                padx=10, pady=5)

            row += 1

        self.button = Button(self, text='Volver a jugar', command=lambda: [
                            self.master.cambia_frame(Inicio, self.master)], font=(constantes.tipografia, 6, 'bold'))
        self.button.grid(row=12, column=0, sticky='nsew', padx=0, pady=0)
        self.button.config(bg=constantes.color_fondo, fg='white',
                            justify='left',
                            font=(constantes.tipografia, 12))


root = Tk()
a = PantallaRanking(root)
root.mainloop()
