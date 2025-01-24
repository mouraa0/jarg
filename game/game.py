import random
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
    print('error')
    multiplier_amount = 1


def handle_hit():
    global multiplier_amount
    global points_amount
    print(multiplier_amount)
    points_amount += 4 * multiplier_amount

    if multiplier_amount < 4:
        multiplier_amount += 1    


def clean_active_notes(active_notes):
    for note in active_notes:
        if note.missed:
            active_notes.remove(note)
    
    return active_notes


def create_dot(color, lane, click_area):
    asset_str = 'assets/game/'
    keyboard_key = ''

    if color == 'green':
        asset_str += 'green_dot.png'
        keyboard_key = 'd'
    
    elif color == 'red':
        asset_str += 'red_dot.png'
        keyboard_key = 'f'
    
    elif color == 'yellow':
        asset_str += 'yellow_dot.png'
        keyboard_key = 'j'
    
    elif color == 'blue':
        asset_str += 'blue_dot.png'
        keyboard_key = 'k'

    elif color == 'orange':
        asset_str += 'orange_dot.png'
        keyboard_key = 'l'
    
    return Dot(asset_str, lane.x, lane.height, click_area, keyboard_key)


def add_random_dot(active_notes, lanes, click_areas, colors):
    random_lane_index = random.randint(0, len(lanes) - 1)
    random_color = colors[random_lane_index]
    random_lane = lanes[random_lane_index]
    random_click_area = click_areas[random_lane_index]
    
    new_dot = create_dot(random_color, random_lane, random_click_area)
    active_notes.append(new_dot)


def verify_key_stroke(key, active_notes, key_timers, debounce_time, current_time):
    if key_timers[key] > 0 and current_time - key_timers[key] < debounce_time:
        key_timers[key] = current_time
        return
    
    key_timers[key] = current_time

    if key == active_notes[0].keyboard_key:
        did_hit = active_notes[0].handle_click()

        if did_hit:
            handle_hit()
            active_notes.pop(0)

        else:
            handle_miss()



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
    chart_time = 0
    note_index = 0

    lanes = [green_lane, red_lane, yellow_lane, blue_lane, orange_lane]
    click_areas = [green_click_area, red_click_area, yellow_click_area, blue_click_area, orange_click_area]
    colors = ['green', 'red', 'yellow', 'blue', 'orange']

    # chart = [
    #     {"time": 1.0, "dot": create_dot('green', green_lane, green_click_area)},
    #     {"time": 1.5, "dot": create_dot('red', red_lane, red_click_area)},
    #     {"time": 2.0, "dot": create_dot('yellow', yellow_lane, yellow_click_area)},
    #     {"time": 2.5, "dot": create_dot('blue', blue_lane, blue_click_area)},
    #     {"time": 3.0, "dot": create_dot('orange', orange_lane, orange_click_area)},
    #     {"time": 4.0, "dot": create_dot('green', green_lane, green_click_area)},
    #     {"time": 4.0, "dot": create_dot('orange', orange_lane, orange_click_area)},
    # ]

    active_notes = []

    key_timers = {
        'd': 0,
        'f': 0,
        'j': 0,
        'k': 0,
        'l': 0
    }

    debounce_time = 0.2
    elapsed_time = 0

    while True:
        janela.set_background_color((0, 0, 0))

        elapsed_time += janela.delta_time()
        
        if (teclado.key_pressed('esc')):
            return
        
        if (teclado.key_pressed('w')):
            count_points()
        
        for key in key_timers.keys():
            if teclado.key_pressed(key):
                verify_key_stroke(key, active_notes, key_timers, debounce_time, janela.delta_time())
        
        if elapsed_time >= 1:
            add_random_dot(active_notes, lanes, click_areas, colors)

            elapsed_time = 0
        
        green_lane.draw()
        red_lane.draw()
        yellow_lane.draw()
        blue_lane.draw()
        orange_lane.draw()

        for note in active_notes:
            note.move(janela.delta_time())


        active_notes = clean_active_notes(active_notes)

        green_click_area.draw()
        red_click_area.draw()
        yellow_click_area.draw()
        blue_click_area.draw()
        orange_click_area.draw()

        points_area.draw()
        janela.draw_text(get_points_in_string(), points_area.x + 8, points_area.y + points_area.height - 8 - 30, size=30, color=(255, 255, 255), font_name='Arial', bold=True, italic=False)

        multiplier.draw()

        chart_time += janela.delta_time()
        janela.update()
