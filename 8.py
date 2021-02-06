import constantes
def genera_coordenadas_x(inicio, fin):
    bordes = []
    for coordenada in range (inicio, fin + constantes.CELL_SIZE, constantes.CELL_SIZE):
        bordes.append(coordenada)
    return bordes

print(genera_coordenadas_x(80, 80))
