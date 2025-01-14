from PPlay.window import *
from PPlay.keyboard import *
from PPlay.gameimage import *
from PPlay.sprite import *
from game.classes.dot import *
from game.classes.lane import *
from game.classes.click_area import *

global points_amount
global multiplier_amount
global combo_counter
multiplier_amount = 1
points_amount = 0


def get_points_in_string():
    global points_amount
    return str(points_amount)


def count_points():
    global points_amount
    points_amount += 500


def handle_miss():
    global multiplier_amount
    print('here')
    multiplier_amount = 1


def handle_hit():
    global multiplier_amount
    global points_amount
    print(multiplier_amount)
    points_amount += 4 * multiplier_amount

    if multiplier_amount < 4:
        multiplier_amount += 1    


janela = Window(800, 600)
teclado = Keyboard()
lanes_area_width = janela.width / 3

green_lane = Lane('assets/game/lane.png', lanes_area_width, 0, True)
lanes_spacement = (lanes_area_width - (green_lane.width * 4)) / 4
red_lane = Lane('assets/game/lane.png', lanes_area_width - green_lane.width, lanes_spacement)
yellow_lane = Lane('assets/game/lane.png', red_lane.x, lanes_spacement)
blue_lane = Lane('assets/game/lane.png', yellow_lane.x, lanes_spacement)
orange_lane = Lane('assets/game/lane.png', blue_lane.x, lanes_spacement)

green_click_area = ClickArea('assets/game/dot_area.png', green_lane.x, green_lane.height)
red_click_area = ClickArea('assets/game/dot_area.png', red_lane.x, red_lane.height)
yellow_click_area = ClickArea('assets/game/dot_area.png', yellow_lane.x, yellow_lane.height)
blue_click_area = ClickArea('assets/game/dot_area.png', blue_lane.x, blue_lane.height)
orange_click_area = ClickArea('assets/game/dot_area.png', orange_lane.x, orange_lane.height)

green_dot = Dot('assets/game/green_dot.png', green_lane.x, green_lane.height, green_click_area)
red_dot = Dot('assets/game/red_dot.png', red_lane.x, red_lane.height, red_click_area)
yellow_dot = Dot('assets/game/yellow_dot.png', yellow_lane.x, yellow_lane.height, yellow_click_area)
blue_dot = Dot('assets/game/blue_dot.png', blue_lane.x, blue_lane.height, blue_click_area)
orange_dot = Dot('assets/game/orange_dot.png', orange_lane.x, orange_lane.height, orange_click_area)

points_area = GameImage('assets/game/points_area.png')
points_area.set_position((janela.width / 2) - (points_area.width / 2), green_click_area.y + green_click_area.height + 25)

multiplier = GameImage('assets/game/combo_counter_1.png')
multiplier.set_position((janela.width / 2) - (multiplier.width / 2), points_area.y + points_area.height + 25)

def game_loop():
    global points_amount

    while True:
        janela.set_background_color((0, 0, 0))
        if (teclado.key_pressed('esc')):
            return
        
        if (teclado.key_pressed('w')):
            count_points()

        if (teclado.key_pressed('d')):
            hit = green_dot.handle_click()
            if hit:
                handle_hit()
            else:
                handle_miss()
        
        green_lane.draw()
        red_lane.draw()
        yellow_lane.draw()
        blue_lane.draw()
        orange_lane.draw()

        green_dot.move(janela.delta_time())
        red_dot.draw()
        yellow_dot.draw()
        blue_dot.draw()
        orange_dot.draw()

        green_click_area.draw()
        red_click_area.draw()
        yellow_click_area.draw()
        blue_click_area.draw()
        orange_click_area.draw()

        points_area.draw()
        janela.draw_text(get_points_in_string(), points_area.x + 8, points_area.y + points_area.height - 8 - 30, size=30, color=(255, 255, 255), font_name='Arial', bold=True, italic=False)

        multiplier.draw()

        janela.update()
