from PPlay.window import *
from PPlay.sprite import *
from difficulty.difficulty import difficulty_loop
from ranking.ranking import ranking_loop

game_title = 'JARG'

janela = Window(800, 600)
janela.set_title(game_title)

mouse = Window.get_mouse()

button_jogar = Sprite('assets/menu/jogar.png')
button_jogar.set_position(20, 180)

button_ranking = Sprite('assets/menu/ranking.png')
button_ranking.set_position(20, 240)

button_sair = Sprite('assets/menu/sair.png')
button_sair.set_position(20, 360)

while True:
    janela.set_background_color((0, 0, 0))

    if (mouse.is_over_object(button_jogar) and mouse.is_button_pressed(1)):
        difficulty_loop(janela)
    
    if (mouse.is_over_object(button_ranking) and mouse.is_button_pressed(1)):
        ranking_loop()

    if (mouse.is_over_object(button_sair) and mouse.is_button_pressed(1)):
        break

    janela.draw_text('JARG', 20, 20, size=30, color=(255, 255, 255), font_name='Arial', bold=True, italic=False)
    janela.draw_text('Just Another Rhythm Game', 20, 50, size=30, color=(255, 255, 255), font_name='Arial', bold=True, italic=False)

    button_jogar.draw()
    button_ranking.draw()
    button_sair.draw()
    janela.update()