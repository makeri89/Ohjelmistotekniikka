class ShotCounter:
    def __init__(self):
        self.counter = 0

    def plus_one(self):
        self.counter += 1

    def get_shots(self):
        return self.counter

    def reset(self):
        self.counter = 0
