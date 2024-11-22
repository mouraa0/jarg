from PPlay.window import *
from PPlay.keyboard import *
from PPlay.gameimage import *

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
        janela.update()
