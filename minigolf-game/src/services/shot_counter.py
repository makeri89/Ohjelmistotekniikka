class ShotCounter:
    """A class to keep track of shots made in a game.
    """

    def __init__(self):
        self.counter = 0

    def plus_one(self):
        self.counter += 1

    def get_shots(self):
        return self.counter

    def reset(self):
        self.counter = 0
