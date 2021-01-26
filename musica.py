def play():
    pygame.mixer.music.load('audio\snake.mp3')
    pygame.mixer.music.play()


Button(raiz, text="Play", command=play).grid(
    row=2, column=2, sticky='nsew', padx=10, pady=10)


Background Music:
0:00 - Main Menu
0:18 - Gameplay

Sound Effects:
0:31 - Victory
0:35 - Game Over
0:39 - Select (menu)
0:40 - Fruit
0:41 - Fail
0:43 - Bomb
0:46 - Power Up
