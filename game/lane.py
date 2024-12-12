from PPlay.gameimage import *

class Lane(GameImage):
    def __init__(self, path=str, initial_x=int, increment_x=int, is_first_lane=False):
        super().__init__(path)
        if (is_first_lane):
            self.set_position(initial_x - (self.width / 2), 0)
        else:
            self.set_position(initial_x + self.width + increment_x, 0)
        # self.set_curr_frame(0)
        # self.set_total_duration(1000)
        # self.set_sequence(0, 0, 0, 0)

    # def set_sequence(self, start, end, repeat, speed):
    #     self.set_curr_frame(start)
    #     self.set_total_duration(speed)
    #     self.set_sequence(start, end, repeat)

    # def update(self):
    #     self.draw()