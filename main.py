from PPlay.window import *
from PPlay.sprite import *
from difficulty.difficulty import difficulty_loop

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
    janela.set_background_color((0, 0, 0))

    if (mouse.is_over_object(button_jogar) and mouse.is_button_pressed(1)):
        difficulty_loop(janela)
    
    # if (mouse.is_over_object(button_ranking) and mouse.is_button_pressed(1)):
    #     stats_loop(Stat('20/20/2000', '20:20', 100, 10, 0))

    if (mouse.is_over_object(button_sair) and mouse.is_button_pressed(1)):
        break

    button_jogar.draw()
    button_ranking.draw()
    button_sair.draw()
    janela.update()