comida_coordenadas = (290, 350)
cabeza_coordenadas = [(350, 350), (330, 350)]
cuerpo_coordenadas = [(290, 370), (330, 350), comida_coordenadas]
""" while True:
            if not comida_coordenadas in (cabeza_coordenadas and cuerpo_coordenadas):
                for coordenada_X, coordenada_Y in comida_coordenadas:
                    print('hola')
                    break """

print(cuerpo_coordenadas[:-1])
x, y = comida_coordenadas
print(f'La ex es: {x} y la y es: {y}')

nuevo = [(4, 5)] + cabeza_coordenadas
print(nuevo)
print(cuerpo_coordenadas[1:])
