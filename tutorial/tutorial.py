from PPlay.keyboard import *
from game.game import game_loop

def tutorial_loop(janela, dificuldade):
    teclado = Keyboard()

    while True:
        janela.set_background_color((0, 0, 0))

        if (teclado.key_pressed('space')):
            return game_loop(janela, dificuldade)

        janela.draw_text('Tutorial', 20, 20, size=30, color=(255, 255, 255), font_name='Arial', bold=True, italic=False)

        janela.draw_text('Linha Verde (Primeira): D', 20, 100, size=30, color=(255, 255, 255))
        janela.draw_text('Linha Vermelha (Segunda): F', 20, 150, size=30, color=(255, 255, 255))
        janela.draw_text('Linha Amarela (Terceira): J', 20, 200, size=30, color=(255, 255, 255))
        janela.draw_text('Linha Azul (Quarta): K', 20, 250, size=30, color=(255, 255, 255))
        janela.draw_text('Linha Laranja (Quinta): L', 20, 300, size=30, color=(255, 255, 255))

        janela.draw_text('Pressione as teclas no momento certo para pontuar', 20, 400, size=30, color=(255, 255, 255))

        janela.draw_text('Pressione ESPAÇO para continuar', 20, janela.height - 80, size=30, color=(255, 255, 255))

        janela.update()
