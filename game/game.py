import datetime
import random
from PPlay.window import *
from PPlay.keyboard import *
from PPlay.gameimage import *
from PPlay.sprite import *
from game.classes.dot import *
from game.classes.lane import *
from game.classes.click_area import *
from game.classes.multiplier import *
from stats.classes.stat import Stat
from stats.stats import stats_loop

global points_amount
global multiplier_amount
global multiplier_streak_amount
global combo_counter
global total_misses
global highest_streak
global actual_streak

multiplier_amount = 1
actual_streak = 0
multiplier_streak_amount = 0
points_amount = 0
highest_streak = 0
total_misses = 0


def get_points_in_string():
    global points_amount
    return str(points_amount)


def count_points():
    global points_amount
    points_amount += 500


def handle_miss(click_area):
    global multiplier_amount
    global multiplier_streak_amount
    global total_misses
    global actual_streak
    global highest_streak

    click_area.miss()
    multiplier_amount = 1
    multiplier_streak_amount = 0
    total_misses += 1

    if actual_streak > highest_streak:
        highest_streak = actual_streak

    actual_streak = 0


def handle_hit():
    global multiplier_amount
    global multiplier_streak_amount
    global points_amount
    global actual_streak

    actual_streak += 1

    points_amount += 4 * multiplier_amount

    if multiplier_amount == 4:
        return

    if multiplier_streak_amount < 3:
        multiplier_streak_amount += 1

        return

    if multiplier_amount == 3 and multiplier_streak_amount == 3:
        multiplier_amount += 1
        multiplier_streak_amount = 3

        return

    multiplier_amount += 1
    multiplier_streak_amount = 0  


def clean_active_notes(active_notes):
    for note in active_notes:
        if note.missed:
            handle_miss(note.click_area)
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


def verify_key_stroke(key, active_notes, click_areas):
    if key == active_notes[0].keyboard_key:
        did_hit = active_notes[0].handle_click()

        if did_hit:
            handle_hit()
            active_notes.pop(0)

        else:
            handle_miss(get_click_area_by_key(key, click_areas))
        
        return
    
    handle_miss(get_click_area_by_key(key, click_areas))


def get_click_area_by_key(key, click_areas):
    if (key == 'd'):
        return click_areas[0]
    
    if (key == 'f'):
        return click_areas[1]

    if (key == 'j'):
        return click_areas[2]
    
    if (key == 'k'):
        return click_areas[3]
    
    if (key == 'l'):
        return click_areas[4]


def get_maximum_elapsed_time(difficulty):
    if difficulty == 'easy':
        return 1

    if difficulty == 'medium':
        return 0.5

    if difficulty == 'hard':
        return 0.25


def get_countdown_time(difficulty):
    if difficulty == 'easy':
        return 30

    if difficulty == 'medium':
        return 60

    if difficulty == 'hard':
        return 90


def format_countdown(countdown):
    if countdown > 60:
        minutes = int(countdown // 60)
        seconds = int(countdown % 60)
        return f"{minutes:02}:{seconds:02}"
    else:
        return str(round(countdown))
    

def end_game():
    global points_amount
    global highest_streak
    global total_misses

    current_time = datetime.datetime.now()
    date_str = current_time.strftime("%d/%m/%Y")
    time_str = current_time.strftime("%H:%M")

    if highest_streak < actual_streak:
        highest_streak = actual_streak

    return stats_loop(Stat(date_str, time_str, points_amount, highest_streak, total_misses), True)
    

def game_loop(janela, difficulty='easy'):
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

    points_area = GameImage('assets/game/points_area.png')
    points_area.set_position((janela.width / 2) - (points_area.width / 2), green_click_area.y + green_click_area.height + 25)

    multiplier = Multiplier('assets/game/combo_counters/combo_counter_1_0.png', (janela.width / 2), points_area.y + points_area.height + 25)

    global points_amount
    global multiplier_amount
    global multiplier_streak_amount
    global combo_counter
    global total_misses
    global highest_streak
    global actual_streak

    multiplier_amount = 1
    actual_streak = 0
    multiplier_streak_amount = 0
    points_amount = 0
    highest_streak = 0
    total_misses = 0

    chart_time = 0

    lanes = [green_lane, red_lane, yellow_lane, blue_lane, orange_lane]
    click_areas = [green_click_area, red_click_area, yellow_click_area, blue_click_area, orange_click_area]
    colors = ['green', 'red', 'yellow', 'blue', 'orange']

    active_notes = []

    keys = ['d', 'f', 'j', 'k', 'l']

    debounce_time = 0.2
    click_time = 0
    elapsed_time = 0
    maximum_elapsed_time = get_maximum_elapsed_time(difficulty)
    countdown = get_countdown_time(difficulty)
    initial_countdown = 0
    initial_countdown_limit = 2
    final_countdown = 0
    game_started = False

    while True:
        janela.set_background_color((0, 0, 0))

        if game_started:
            elapsed_time += janela.delta_time()
        
        if countdown <= 0 and len(active_notes) == 0:
            final_countdown += janela.delta_time()

            if final_countdown >= 2:
                return end_game()

        if initial_countdown < initial_countdown_limit:
            initial_countdown += janela.delta_time()

        if initial_countdown >= initial_countdown_limit and not game_started:
            game_started = True

        if click_time != 0:
            click_time += janela.delta_time()

            if click_time >= debounce_time:
                click_time = 0

        if countdown > 0 and game_started:
            countdown -= janela.delta_time()
        
        if (teclado.key_pressed('esc')):
            return

        for key in keys:
            if teclado.key_pressed(key) and click_time == 0:
                click_time += janela.delta_time()
                verify_key_stroke(key, active_notes, click_areas)
        
        if elapsed_time >= maximum_elapsed_time and countdown >= 0 and game_started:
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

        green_click_area.update()
        red_click_area.update()
        yellow_click_area.update()
        blue_click_area.update()
        orange_click_area.update()

        points_area.draw()
        janela.draw_text(get_points_in_string(), points_area.x + 8, points_area.y + points_area.height - 8 - 30, size=30, color=(255, 255, 255), font_name='Arial', bold=True, italic=False)
        janela.draw_text(format_countdown(countdown), 20, 20, size=30, color=(255, 255, 255), font_name='Arial', bold=True, italic=False)

        multiplier.update(multiplier_amount, multiplier_streak_amount)

        chart_time += janela.delta_time()
        janela.update()
