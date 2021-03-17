import pygame


class Clock:
    """A class for pygame clock to be used in the main game
    """

    def __init__(self):
        self.clock = pygame.time.Clock()

    def tick(self, fps):
        self.clock.tick(fps)
