from random import randint

class Die:
    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        # return from 1 to 6
        return randint(1, self.num_sides)