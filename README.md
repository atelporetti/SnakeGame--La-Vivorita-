# SnakeGame-LaVivorita
_Clasico juego de La Vivorita_

En este juego, el jugador utiliza las teclas de flecha para mover una "serpiente" alrededor del tablero. A medida que la serpiente encuentra comida, se la come, y así crece. El juego termina cuando la serpiente sale de la pantalla o se mueve hacia sí misma. El objetivo es hacer que la serpiente sea lo más grande posible antes de que eso ocurra.

### Instalación 🔧

_1. Instalar las fuentes ubicadas dentro de la carpeta 'fonts'_

_2. Instalar pygame:_

      python3 -m pip install -U pygame --user
      
o si no funciona:

      pip pygame install
      
_3. Instalar pandas:_

      python3 -m pip install pandas
 
 o si no funciona:

      pip pandas install
      

## Construido con 🛠️

* Python 🐍 v 3.9.1
* Librerias:
  * tkinter (Interfaz gráfica de usuario)
  * pygame (uso: Reproducción de sonidos)
  * pandas (uso: gestión de datos)

# Funcionalidades

* Introducir 'Nombre de Jugador'
* Selección de 'Nivel de Dificultad' (cambia la velocidad en que la vivorita se desplaza inicialmente por la pantalla y en la que se incrementa gradualmente su velocidad)
* Validación de Campos
* Música ON/OFF

![LaVivorita_inicio_GIF](https://user-images.githubusercontent.com/69491395/109424349-0b971880-79c2-11eb-9bf6-f282046f0046.gif)


## Ejemplo de partida

![LaVivorita_partida_GIF](https://user-images.githubusercontent.com/69491395/109424066-e6ee7100-79c0-11eb-85a1-376262002583.gif)

* Registro de datos de la partida: Nombre de Jugador, Puntaje, Nivel de Dificultad y Tiempo de Juego(seg.)
* Comprobación de mejor partida histórica

![LaVivorita_puntaje_alto](https://user-images.githubusercontent.com/69491395/109424487-8bbd7e00-79c2-11eb-9233-8f2be68d9507.png)
![LaVivorita_fin_juego](https://user-images.githubusercontent.com/69491395/109424380-249fc980-79c2-11eb-834a-7899f0d37781.png)
