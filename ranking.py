import csv
import pandas as pd

class Ranking:
    def __init__(self, puntaje, jugador, tiempo, ubicacion_archivo):
        self.puntaje = puntaje
        self.jugador = jugador
        self.tiempo = tiempo
        self.ubicacion_archivo = ubicacion_archivo

    def ordena_puntaje_cvs(self):
        ranking = pd.read_csv(self.ubicacion_archivo, sep=',')
        ranking = ranking.sort_values(['Puntaje'], ascending=False)
        ranking = ranking.to_csv(self.ubicacion_archivo, index = False)
        
    def guarda_partida_csv(self):
        with open(self.ubicacion_archivo, mode='a') as archivo_csv:
            campos = ['Puntaje', 'Jugador', 'Tiempo']
            csv_escrito = csv.DictWriter(archivo_csv, fieldnames=campos, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            #csv_escrito.writeheader()
            csv_escrito.writerow({'Puntaje': self.puntaje, 'Jugador': self.jugador, 'Tiempo': self.tiempo})

    def es_puntaje_alto(self):
        ranking = pd.read_csv(self.ubicacion_archivo, sep=',')
        return self.puntaje > ranking['Puntaje'].max()