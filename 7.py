import csv, constantes

def abre(ubicacion):
    with open(ubicacion, 'r') as reader:
        # Note: readlines doesn't trim the line endings
        dog_breeds = reader.readlines()
        return dog_breeds

def guarda(ubicacion):
    with open(ubicacion, 'w') as writer:
        # Alternatively you could use
        # writer.writelines(reversed(dog_breeds))

        # Write the dog breeds to the file in reversed order
        for breed in abre('Assets/other/ranking_puntajes.txt'):
            writer.write(breed)

#guarda('Assets/other/ranking.txt')

def abre_cvs(ubicacion):
    with open(ubicacion, mode='r') as archivo_csv:
        csv_leido = csv.DictReader(archivo_csv, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        line_count = 0
        for row in csv_leido:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            print(f'\t{row["Puntaje"]} {row["Jugador"]} {row["Tiempo"]}')
            line_count += 1
        print(f'Processed {line_count} lines.')

def guarda_csv(ubicacion):
    with open(ubicacion, mode='a') as archivo_csv:
        campos = ['Puntaje', 'Jugador', 'Tiempo']
        csv_escrito = csv.DictWriter(archivo_csv, fieldnames=campos, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_escrito.writeheader()
        csv_escrito.writerow({'Puntaje': '15', 'Jugador': 'Cashlos', 'Tiempo': '450'})

abre_cvs('Assets/other/ranking.csv')
guarda_csv('Assets/other/ranking.csv')

