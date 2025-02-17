import json
from PPlay.keyboard import *
from PPlay.window import *
from stats.classes.stat import Stat

def save_stat(stat):
    try:
        with open('ranking/ranking.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []

    data.append({
        'date': stat.date,
        'hour': stat.hour,
        'score': stat.score,
        'highest_streak': stat.highest_streak,
        'misses': stat.misses
    })

    with open('ranking/ranking.json', 'w') as file:
        json.dump(data, file, indent=4)

        
janela = Window(800, 600)
teclado = Keyboard()

def stats_loop(stat=Stat, is_end_game=False):
    if is_end_game:
        save_stat(stat)
    
    while True:
        janela.set_background_color((0, 0, 0))

        janela.draw_text('Stats', 20, 20, size=30, color=(255, 255, 255), font_name='Arial', bold=True, italic=False)

        janela.draw_text(f'Data: {stat.date}', 20, 100, size=30, color=(255, 255, 255))
        janela.draw_text(f'Hora: {stat.hour}', 20, 150, size=30, color=(255, 255, 255))
        janela.draw_text(f'Score: {stat.score}', 20, 200, size=30, color=(255, 255, 255))
        janela.draw_text(f'Maior streak: {stat.highest_streak}', 20, 250, size=30, color=(255, 255, 255))
        janela.draw_text(f'Erros: {stat.misses}', 20, 300, size=30, color=(255, 255, 255))

        distance = 400 if is_end_game else 350

        janela.draw_text(f'Aperte ESC para {"continuar" if is_end_game else "voltar"}', janela.width - distance, janela.height - 80, size=30, color=(255, 255, 255))

        if (teclado.key_pressed('esc')):
            return

        janela.update()

