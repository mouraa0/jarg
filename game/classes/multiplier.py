from PPlay.gameimage import *


class Multiplier():
    def __init__(self, path=str, x=int, y=int):
        self.game_image = GameImage(path)
        self.game_image.set_position(x - (self.game_image.width / 2) + 1, y)
        self.actual_value = 1
        self.current_streak = 0
    
    def update(self, multiplier_amount, multiplier_streak):
        if multiplier_amount != self.actual_value or multiplier_streak != self.current_streak:
            self.update_multiplier(multiplier_amount, multiplier_streak)

        self.game_image.draw()
    
    def update_multiplier(self, multiplier_amount, multiplier_streak):
        new_image = GameImage(f'assets/game/combo_counters/combo_counter_{multiplier_amount}_{multiplier_streak}.png')
        new_image.set_position(self.game_image.x, self.game_image.y)

        self.game_image = new_image
        self.actual_value = multiplier_amount
        self.current_streak = multiplier_streak
