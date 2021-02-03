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

#------- COMMANDS KEYBOARD -------
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'
#---------------------------------

#------------ IMAGES ------------
imagen_fondo = 'Assets/img/snake_welcome658x288.png'
icon = 'Assets/img/snake_icon.ico'
titulo = 'La Vivorita: el juego'
tipografia = '8-bit pusab'
cabeza_serpiente = 'Assets/img/snake_head.png' #snake_head2_20x20
cuerpo_serpiente = 'Assets/img/snake_body.png' #snake_body_20x20
#---------------------------------

#------------ COLORS ------------
color_tipografia = '#B2BD08'
color_cabeza = '#B2BD08'
color_cuerpo = '#B2BD59'
color_obstaculo = '#B22B00'
color_fondo = 'black'
#---------------------------------

#------------- MUSIC -------------
musica_inicio = 'Assets/audio/inicio.wav'
musica_en_juego = 'Assets/audio/en_movimiento.wav'
musica_fin = 'Assets/audio/game_over.wav'
musica_play = 'Assets/audio/power_up.wav'
#---------------------------------


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

direction_vectors = {
    "Up": (0, -1),
    "Down": (0, 1),
    "Left": (-1, 0),
    "Right": (1, 0),
}
