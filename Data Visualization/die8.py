from random import randint


class Die():
    """ A class representing a single die. """
    def __init__(self, num_sides=8):
        # Assume a six-sided die above.
        self.num_sides = num_sides

    def roll(self):
        # Return a random value between 1 and num_sides.
        return randint(1, self.num_sides)
