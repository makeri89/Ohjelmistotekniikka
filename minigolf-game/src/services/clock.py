import pygame


class Clock:
    """A class for pygame clock to be used in the main game."""

    def __init__(self):
        """Initializes a pygame clock."""
        self.clock = pygame.time.Clock()

    def tick(self, fps):
        """A method to make the clock tick.

        Args:
            fps: Frames per second
        """
        self.clock.tick(fps)
