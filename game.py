from PPlay.window import *
from PPlay.keyboard import *
from PPlay.gameimage import *
from PPlay.sprite import *

janela = Window(800, 600)
teclado = Keyboard()

green_lane = GameImage('assets/game/lane.png')
red_lane = GameImage('assets/game/lane.png')
yellow_lane = GameImage('assets/game/lane.png')
blue_lane = GameImage('assets/game/lane.png')
orange_lane = GameImage('assets/game/lane.png')

lanes_area_width = janela.width / 3
lanes_spacement = (lanes_area_width - (green_lane.width * 4)) / 4

green_lane.set_position(lanes_area_width - (green_lane.width / 2) , 0)
red_lane.set_position(lanes_area_width + lanes_spacement, 0)
yellow_lane.set_position(red_lane.x + red_lane.width + lanes_spacement, 0)
blue_lane.set_position(yellow_lane.x + red_lane.width + lanes_spacement, 0)
orange_lane.set_position(blue_lane.x + red_lane.width + lanes_spacement, 0)

green_dot = Sprite('assets/game/green_dot.png')
red_dot = Sprite('assets/game/red_dot.png')
yellow_dot = Sprite('assets/game/yellow_dot.png')
blue_dot = Sprite('assets/game/blue_dot.png')
orange_dot = Sprite('assets/game/orange_dot.png')

green_dot.set_position(green_lane.x - (green_dot.width / 2) + 1, green_lane.height / 2)
red_dot.set_position(red_lane.x - (red_dot.width / 2) + 1, red_lane.height / 2)
yellow_dot.set_position(yellow_lane.x - (yellow_dot.width / 2) + 1, yellow_lane.height / 2)
blue_dot.set_position(blue_lane.x - (blue_dot.width / 2) + 1, blue_lane.height / 2)
orange_dot.set_position(orange_lane.x - (orange_dot.width / 2) + 1, orange_lane.height / 2)

green_dot_area = Sprite('assets/game/dot_area.png')
red_dot_area = Sprite('assets/game/dot_area.png')
yellow_dot_area = Sprite('assets/game/dot_area.png')
blue_dot_area = Sprite('assets/game/dot_area.png')
orange_dot_area = Sprite('assets/game/dot_area.png')

green_dot_area.set_position(green_lane.x - (green_dot_area.width / 2) + 1, green_lane.height)
red_dot_area.set_position(red_lane.x - (red_dot_area.width / 2) + 1, red_lane.height)
yellow_dot_area.set_position(yellow_lane.x - (yellow_dot_area.width / 2) + 1, yellow_lane.height)
blue_dot_area.set_position(blue_lane.x - (blue_dot_area.width / 2) + 1, blue_lane.height)
orange_dot_area.set_position(orange_lane.x - (orange_dot_area.width / 2) + 1, orange_lane.height)


def game_loop():
    janela.set_background_color((0, 0, 0))

    while True:
        if (teclado.key_pressed('esc')):
            return
        
        green_lane.draw()
        red_lane.draw()
        yellow_lane.draw()
        blue_lane.draw()
        orange_lane.draw()

        green_dot.draw()
        red_dot.draw()
        yellow_dot.draw()
        blue_dot.draw()
        orange_dot.draw()

        green_dot_area.draw()
        red_dot_area.draw()
        yellow_dot_area.draw()
        blue_dot_area.draw()
        orange_dot_area.draw()

        janela.update()
