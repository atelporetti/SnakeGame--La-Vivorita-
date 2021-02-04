width = 40
height = 20
step_len = 2 * height

grid = {
    "tamanio": width * height,
    "background_color": "grey",

}
filas = 5
columnas = 1
#------------ SCREEN -------------
WINDOW_WIDTH = 720
WINDOW_HEIGHT = 700
CELL_SIZE = 20
assert WINDOW_WIDTH % CELL_SIZE == 0, 'El tamaño de la celda debe ser siempre multiplo del ancho de la ventana.'
assert WINDOW_HEIGHT % CELL_SIZE == 0, 'El tamaño de la celda debe ser siempre multiplo del alto de la ventana'
CELL_WIDTH = int(WINDOW_WIDTH / CELL_SIZE)
CELL_HEIGHT = int(WINDOW_HEIGHT / CELL_SIZE)
CANVA_WIDTH = 680
CANVA_HEIGHT = 620
CELL_CANVA_WIDTH = int(CANVA_WIDTH / CELL_SIZE)
CELL_CANVA_HEIGHT = int(CANVA_HEIGHT / CELL_SIZE)
#---------------------------------

#------- COMMANDS KEYBOARD -------
DIRECCIONES_FLECHAS = ('Left', 'Right', 'Up', 'Down')
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
comida = 'Assets/img/comida.png'
hueco = 'Assets/img/hueco.png'
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

#------------- SNAKE -------------
MOVIMIENTOS_POR_SEGUNDO = 12
VELOCIDAD = 1000 // MOVIMIENTOS_POR_SEGUNDO # Se divide por mil ya que la funcion after() toma el tiempo en milisegundos


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
    "Arriba": (0, -1),
    "Abajo": (0, 1),
    "Izquierda": (-1, 0),
    "Derecha": (1, 0),
}
