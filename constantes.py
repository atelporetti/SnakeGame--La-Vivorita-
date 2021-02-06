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
assert CANVA_WIDTH % CELL_SIZE == 0, 'El tamaño de la celda debe ser siempre multiplo del ancho de la ventana.'
assert CANVA_HEIGHT % CELL_SIZE == 0, 'El tamaño de la celda debe ser siempre multiplo del alto de la ventana'
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
cabeza_serpiente = 'Assets/img/cabeza_serpiente.png'
cuerpo_serpiente = 'Assets/img/cuerpo_serpiente.png'
comida_violeta = 'Assets/img/comida_violeta.png'
comida_roja = 'Assets/img/comida_rojo.png'
comida_amarilla = 'Assets/img/comida_amarillo.png'
comida_azul = 'Assets/img/comida_azul.png'
comida_fucsia = 'Assets/img/comida_fucsia.png'
comida_naranja = 'Assets/img/comida_naranja.png'
comida_verde = 'Assets/img/comida_verde.png'
comidas = [comida_violeta, comida_roja, comida_amarilla, comida_azul, comida_fucsia, comida_naranja]
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
musica_comida = 'Assets/audio/comer_fruta.wav'
musica_colision = 'Assets/audio/choque.wav'
musica_victoria = 'Assets/audio/victoria.wav'
#---------------------------------

#------------- SNAKE -------------
movimientos_por_segundo = 12
VELOCIDAD = 1000 // movimientos_por_segundo # Se divide por mil ya que la funcion after() toma el tiempo en milisegundos
#---------------------------------

#------------- ARCHIVOS -------------
RANKING = 'Assets/other/ranking.csv'
VELOCIDAD = 1000 // movimientos_por_segundo # Se divide por mil ya que la funcion after() toma el tiempo en milisegundos
#---------------------------------