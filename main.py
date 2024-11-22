from PPlay.window import *
from PPlay.sprite import *
from game import game_loop

game_title = 'JARG'

janela = Window(800, 600)
janela.set_title(game_title)

mouse = Window.get_mouse()

button_jogar = Sprite('assets/menu/jogar.png')
button_jogar.set_position(30, 120)

button_ranking = Sprite('assets/menu/ranking.png')
button_ranking.set_position(30, 180)

button_sair = Sprite('assets/menu/sair.png')
button_sair.set_position(30, 240)

while True:
    if (mouse.is_over_object(button_jogar) and mouse.is_button_pressed(1)):
        game_loop()

    if (mouse.is_over_object(button_sair) and mouse.is_button_pressed(1)):
        break

    button_jogar.draw()
    button_ranking.draw()
    button_sair.draw()
    janela.update()