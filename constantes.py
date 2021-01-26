width = 40
height = 20
step_len = 2 * height

grid = {
    "tamanio": width * height,
    "background_color": "grey",

}
filas = 5
columnas = 2
imagen_fondo = 'img/snakeWelcome658x288.png'
icon = 'img/snake.ico'
titulo = 'La Vivorita: el juego'
tipografia = '8-bit pusab'

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
