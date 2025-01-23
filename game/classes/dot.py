from PPlay.sprite import *
from PPlay.gameimage import *

class Dot(Sprite):
    def __init__(self, path=str, lane_x=int, lane_y=int, click_area=GameImage, keyboard_key=str):
        super().__init__(path)
        self.set_position(lane_x - (self.width / 2) + 1, 0)
        self.initial_height = 0
        self.click_area = click_area
        self.points = 4
        self.center_y = self.height / 2
        self.keyboard_key = keyboard_key
        self.missed = False
        # self.set_curr_frame(0)
        # self.set_total_duration(1000)
        # self.set_sequence(0, 0, 0, 0)


    def move(self, delta_time):
        self.y += 140 * delta_time

        if self.y > self.click_area.y + self.click_area.height + 10:
            self.missed = True
        
        self.draw()

    def handle_click(self):
        hit = False

        if self.y + self.height > self.click_area.y - 10:
            hit = True

        return hit
        

    # def set_sequence(self, start, end, repeat, speed):
    #     self.set_curr_frame(start)
    #     self.set_total_duration(speed)
    #     self.set_sequence(start, end, repeat)

    # def update(self):
    #     self.draw()
