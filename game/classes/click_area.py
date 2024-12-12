from PPlay.sprite import *

class ClickArea(Sprite):
    def __init__(self, path=str, lane_x=int, lane_y=int):
        super().__init__(path)
        self.set_position(lane_x - (self.width / 2) + 1, lane_y)
        # self.set_curr_frame(0)
        # self.set_total_duration(1000)
        # self.set_sequence(0, 0, 0, 0)

    # def set_sequence(self, start, end, repeat, speed):
    #     self.set_curr_frame(start)
    #     self.set_total_duration(speed)
    #     self.set_sequence(start, end, repeat)

    # def update(self):
    #     self.draw()