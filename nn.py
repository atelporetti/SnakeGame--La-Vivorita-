from threading import *
import time
def manejarCliente1():
    while(True):
        print("Esperando al cliente 1...")
        time.sleep(3) # Espera 3 segundos     
def manejarCliente2():
    while(True):
        print("Esperando al cliente 2...")
        time.sleep(3) # Espera 3 segundos
# Creacion de los hilos
t = Timer(8.0, manejarCliente1)
t2 = Timer(3.0, manejarCliente2)
# Ejecutar los hilos
t.start()
t2.start()