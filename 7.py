cuerpo_coordenadas = [(0, 680), (300, 300)]
print(cuerpo_coordenadas)

coordenada_X, coordenada_Y = cuerpo_coordenadas[0]
coords = (coordenada_X, coordenada_Y)
print(cuerpo_coordenadas[0])
print(coordenada_X, coordenada_Y)
print(coords)
if not coordenada_X in (0, 680) and not coordenada_Y in (0, 620):
    print('no toco los limites')
else:
    print('toco los limites')
