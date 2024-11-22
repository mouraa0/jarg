from PPlay.window import *
from PPlay.keyboard import *

janela = Window(800, 600)
teclado = Keyboard()

def game_loop():
    while True:
        if (teclado.key_pressed('esc')):
            return

        janela.set_background_color((0, 0, 0))
        janela.update()
