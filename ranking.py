import csv
import pandas as pd
try:
    from tkinter import Frame
except:
    from Tkinter import Frame


class Ranking():
    def __init__(self, puntaje, jugador, tiempo, ubicacion_archivo):
        self.puntaje = puntaje
        self.jugador = jugador
        self.tiempo = tiempo
        self.ubicacion_archivo = ubicacion_archivo

    def ordena_puntaje_cvs(self):
        ranking = pd.read_csv(self.ubicacion_archivo, sep=',')
        ranking = ranking.sort_values(['Puntaje'], ascending=False)
        ranking.to_csv(self.ubicacion_archivo, index=False)

    def guarda_partida_csv(self):
        ranking = pd.read_csv(self.ubicacion_archivo, sep=',')
        datos = {
            'Puntaje': [self.puntaje],
            'Jugador': [self.jugador],
            'Tiempo': [self.tiempo]
        }
        data_frame = pd.DataFrame.from_dict(datos)
        ranking = ranking.append(data_frame,sort=False)
        ranking.to_csv(self.ubicacion_archivo, index=False)

    def es_puntaje_alto(self):
        ranking = pd.read_csv(self.ubicacion_archivo, sep=',')
        return self.puntaje > ranking['Puntaje'].max()

    def lee_n_lineas(self, numero):
        ranking = pd.read_csv(self.ubicacion_archivo,
                              nrows=numero, sep=',', skiprows=1)
        ranking.shape()


class PantallaRanking(Frame):
    pass
