import json
from PPlay.keyboard import *
from PPlay.window import *
from stats.classes.stat import *
from stats.stats import stats_loop


def get_top_5_stats():
    try:
        with open('ranking/ranking.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        return []

    sorted_data = sorted(data, key=lambda x: x['score'], reverse=True)
    top_5_data = sorted_data[:5]
    top_5_stats = [Stat(d['date'], d['hour'], d['score'], d['highest_streak'], d['misses']) for d in top_5_data]

    return top_5_stats


janela = Window(800, 600)
teclado = Keyboard()

def ranking_loop():
    stats = get_top_5_stats()

    debounce_time = 0.7
    click_time = 0

    while True:
        if click_time != 0:
            click_time += janela.delta_time()

            if click_time >= debounce_time:
                click_time = 0

        janela.set_background_color((0, 0, 0))

        if teclado.key_pressed('esc') and click_time == 0:
            print('here')
            return

        for i in range(len(stats)):
            if teclado.key_pressed(str(i + 1)):
                stats_loop(stats[i])

                click_time += janela.delta_time()

        janela.draw_text('Ranking', 20, 20, size=30, color=(255, 255, 255), font_name='Arial', bold=True, italic=False)

        for i in range(len(stats)):
            stat = stats[i]
            janela.draw_text(f'{i + 1}. {stat.date} {stat.hour} - {stat.score} pts', 20, 100 + i * 50, size=30, color=(255, 255, 255))

        janela.draw_text('Aperte o número referente a posição para mais detalhes, ou ESC para voltar', 20, janela.height - 80, size=18, color=(255, 255, 255))

        janela.update()