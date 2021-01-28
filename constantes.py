width = 40
height = 20
step_len = 2 * height

grid = {
    "tamanio": width * height,
    "background_color": "grey",

}
filas = 5
columnas = 2
#------------ SCREEN -------------
WINDOW_HEIGHT = 700
WINDOW_WIDTH = 720
CELL_SIZE = 20
assert WINDOW_HEIGHT % CELL_SIZE == 0, 'El tamaño de la celda debe ser siempre multiplo del alto de la ventana'
assert WINDOW_WIDTH % CELL_SIZE == 0, 'El tamaño de la celda debe ser siempre multiplo del ancho de la ventana.'
CELL_HEIGHT = int(WINDOW_HEIGHT / CELL_SIZE)
CELL_WIDTH = int(WINDOW_WIDTH / CELL_SIZE)
#---------------------------------

imagen_fondo = 'Assets/img/snakeWelcome658x288.png'
icon = 'Assets/img/snake.ico'
titulo = 'La Vivorita: el juego'
tipografia = '8-bit pusab'
color_tipografia = '#B2BD08'
color_cabeza = '#B2BD08'
color_cola = '#B2BD59'
color_obstaculo = '#B22B00'
musica_inicio = 'Assets/audio/inicio.wav'
musica_play = 'Assets/audio/power_up.wav'
# shapes
snake_factor = 1
obstacle_factor = 0.9

obstacle = {
    "size": height * obstacle_factor,
    "color": "red",
}

snake = {
    "size": height * snake_factor,
    "color": "white",
}

# constants for keyboard input
direction_vectors = {
    "Up": (0, -1),
    "Down": (0, 1),
    "Left": (-1, 0),
    "Right": (1, 0),
}

# refresh time for the perpetual motion
refresh_ms = 100
