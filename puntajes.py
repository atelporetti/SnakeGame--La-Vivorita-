""" try:
    from tkinter import *
except:
    from Tkinter import * """
import csv, constantes
from tkinter import IntVar

class Puntaje:
    def __init__(self, master):
        self.contador = IntVar(master, 0)
        self.maximo = IntVar(master, 0)

    def aumenta(self):
        puntaje = int(self.contador.get()) + 1
        maximo = max(puntaje, int(self.maximo.get()))
        self.contador.set(str(puntaje))
        self.maximo.set(str(maximo))

    def reset(self):
        self.contador.set(0)

    def lee_ordena_archivo(self):
        """ Guarda la lista de puntajes en el archivo.
        Pre: nombre_archivo corresponde a un archivo válido,
        puntajes corresponde a una lista de tuplas de 3 elementos.
        Post: se guardaron los valores en el archivo,
        separados por comas.
        """
        puntajes = []
        nombres = []
        tiempos_juego = []
        with open('Assets/other/ranking_puntajes.txt', 'r+') as ranking_puntajes:
            for linea in ranking_puntajes:
                linea = linea.rstrip()
                puntaje, nombre, tiempo_juego = linea.split()
                puntajes.append(puntaje)
                nombres.append(nombre)
                tiempos_juego.append(tiempo_juego)
            archivo_ordenado = zip(puntajes, nombres)
            print(archivo_ordenado)
            puntajes_ordenados = sorted(puntajes, reverse=True)
            print(puntajes_ordenados)
            archivo_ordenado_ = zip(puntajes_ordenados, nombres, tiempos_juego)
            print(archivo_ordenado_)
            return archivo_ordenado_
    
    def guarda_archivo(self):
        with open('Assets/other/ranking.txt', 'a') as archivo_escrito:
            archivo_escrito.write('\nBeagle')
    
    def abre_cvs(self, ubicacion):
        with open(ubicacion, mode='r') as archivo_csv:
            csv_leido = csv.DictReader(archivo_csv, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for row in csv_leido:
                print(f'\t{row["Puntaje"]} {row["Jugador"]} {row["Tiempo"]}')

    def guarda_csv(self, ubicacion):
        with open(ubicacion, mode='a') as archivo_csv:
            campos = ['Puntaje', 'Jugador', 'Tiempo']
            csv_escrito = csv.DictWriter(archivo_csv, fieldnames=campos, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            #csv_escrito.writeheader()
            csv_escrito.writerow({'Puntaje': '15', 'Jugador': 'Cashlos', 'Tiempo': '450'})

ranking = Puntaje()
#ranking.lee_ordena_archivo()
#ranking.guarda_archivo()
ranking.abre_cvs(constantes.RANKING)
ranking.guarda_csv(constantes.RANKING)
