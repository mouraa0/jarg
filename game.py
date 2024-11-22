from PPlay.window import *
from PPlay.keyboard import *
from PPlay.gameimage import *
from PPlay.sprite import *

global points_amount
points_amount = 0

def get_points_in_string():
    global points_amount
    return str(points_amount)

def count_points():
    global points_amount
    points_amount += 500

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

points_area = GameImage('assets/game/points_area.png')
points_area.set_position((janela.width / 2) - (points_area.width / 2), green_dot_area.y + green_dot_area.height + 25)

combo_counter = GameImage('assets/game/combo_counter_1.png')
combo_counter.set_position((janela.width / 2) - (combo_counter.width / 2), points_area.y + points_area.height + 25)

def game_loop():
    while True:
        janela.set_background_color((0, 0, 0))
        if (teclado.key_pressed('esc')):
            return
        
        if (teclado.key_pressed('w')):
            count_points()
        
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

        points_area.draw()
        janela.draw_text(get_points_in_string(), points_area.x + 8, points_area.y + points_area.height - 8 - 30, size=30, color=(255, 255, 255), font_name='Arial', bold=True, italic=False)

        combo_counter.draw()

        janela.update()
