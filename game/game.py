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


def verify_key_stroke(key, active_notes):
    # if cron != 0:
    #     return

    if teclado.key_pressed(key): 

        if key == active_notes[0].keyboard_key:
            did_hit = active_notes[0].handle_click()

            if did_hit:
                handle_hit()
                active_notes.pop(0)

                # return active_notes

            # return active_notes

        handle_miss()
        # return active_notes

    # return active_notes


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

    click_cron = 0

    chart = [
        {"time": 1.0, "dot": create_dot('green', green_lane, green_click_area)},
        {"time": 1.5, "dot": create_dot('red', red_lane, red_click_area)},
        {"time": 2.0, "dot": create_dot('yellow', yellow_lane, yellow_click_area)},
        {"time": 2.5, "dot": create_dot('blue', blue_lane, blue_click_area)},
        {"time": 3.0, "dot": create_dot('orange', orange_lane, orange_click_area)},
        {"time": 4.0, "dot": create_dot('green', green_lane, green_click_area)},
        {"time": 4.0, "dot": create_dot('orange', orange_lane, orange_click_area)},
    ]

    active_notes = []

    # key_states = {
    #     'd': False,
    #     'f': False,
    #     'j': False,
    #     'k': False,
    #     'l': False
    # }

    while True:
        janela.set_background_color((0, 0, 0))
        
        if (teclado.key_pressed('esc')):
            return
        
        if (teclado.key_pressed('w')):
            count_points()
        
        if note_index < len(chart) and chart[note_index]['time'] < chart_time:
            active_notes.append(chart[note_index]['dot'])
            note_index += 1
        
        if len(active_notes) > 0:
            verify_key_stroke('d', active_notes)
            verify_key_stroke('f', active_notes)
            verify_key_stroke('j', active_notes)
            verify_key_stroke('k', active_notes)
            verify_key_stroke('l', active_notes)
            # if (teclado.key_pressed('d')):
            #     if active_notes[0].keyboard_key == 'd':
            #         hit = active_notes[0].handle_click()
            #         active_notes.pop(0)
            #     if hit:
            #         handle_hit()
            #     else:
            #         handle_miss()
            
            # if (teclado.key_pressed('f')):
            #     if active_notes[0].keyboard_key == 'f':
            #         hit = active_notes[0].handle_click()
            #         active_notes.pop(0)
            #     if hit:
            #         handle_hit()
            #     else:
            #         handle_miss()
            
            # if (teclado.key_pressed('j')):
            #     if active_notes[0].keyboard_key == 'j':
            #         hit = active_notes[0].handle_click()
            #         active_notes.pop(0)
            #     if hit:
            #         handle_hit()
            #     else:
            #         handle_miss()
            
            # if (teclado.key_pressed('k')):
            #     if active_notes[0].keyboard_key == 'k':
            #         hit = active_notes[0].handle_click()
            #         active_notes.pop(0)
            #     if hit:
            #         handle_hit()
            #     else:
            #         handle_miss()
            
            # if (teclado.key_pressed('l')):
            #     if active_notes[0].keyboard_key == 'l':
            #         hit = active_notes[0].handle_click()
            #         active_notes.pop(0)
            #     if hit:
            #         handle_hit()
            #     else:
            #         handle_miss()
        
        green_lane.draw()
        red_lane.draw()
        yellow_lane.draw()
        blue_lane.draw()
        orange_lane.draw()

        for note in active_notes:
            note.move(janela.delta_time())


        active_notes = clean_active_notes(active_notes)


        # green_dot.move(janela.delta_time())
        # red_dot.draw()
        # yellow_dot.draw()
        # blue_dot.draw()
        # orange_dot.draw()

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
