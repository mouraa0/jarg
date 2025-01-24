from PPlay.keyboard import *
from tutorial.tutorial import tutorial_loop

def difficulty_loop(janela):
    teclado = Keyboard()

    while True:
        janela.set_background_color((0, 0, 0))

        janela.draw_text('Selecionar dificuldade', 20, 20, size=30, color=(255, 255, 255), font_name='Arial', bold=True, italic=False)

        janela.draw_text("Aperte '1' para Fácil", 20, 100, size=30, color=(255, 255, 255))
        janela.draw_text("Aperte '2' para Médio", 20, 150, size=30, color=(255, 255, 255))
        janela.draw_text("Aperte '3' para Difícil", 20, 200, size=30, color=(255, 255, 255))

        if teclado.key_pressed('1'):
            return tutorial_loop(janela, 'easy')
        
        if teclado.key_pressed('2'):
            return tutorial_loop(janela, 'medium')
        
        if teclado.key_pressed('3'):
            return tutorial_loop(janela, 'hard')

        janela.update()