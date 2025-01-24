import time
from PPlay.gameimage import *

class ClickArea():
    def __init__(self, path=str, lane_x=int, lane_y=int):
        self.game_image = GameImage(path)
        self.initial_path = path
        self.game_image.set_position(lane_x - (self.game_image.width / 2) + 1, lane_y)
        self.y = self.game_image.y
        self.height = self.game_image.height
        self.hit_timer = 0
        self.miss_timer = 0

    def hit(self):
        self.update_game_image('assets/game/hit_dot_area.png')
        self.hit_timer = time.time()

    def miss(self):
        self.update_game_image('assets/game/miss_dot_area.png')
        self.miss_timer = time.time()

    def update(self):
        current_time = time.time()
        if self.hit_timer and current_time - self.hit_timer >= 0.4:
            self.update_game_image(self.initial_path)
            self.hit_timer = 0
        if self.miss_timer and current_time - self.miss_timer >= 0.4:
            self.update_game_image(self.initial_path)
            self.miss_timer = 0
        self.game_image.draw()
    
    def update_game_image(self, path):
        new_game_image = GameImage(path)
        new_game_image.x = self.game_image.x
        new_game_image.y = self.game_image.y
        new_game_image.width = self.game_image.width
        new_game_image.height = self.game_image.height
        self.game_image = new_game_image