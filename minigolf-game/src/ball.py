import os
import pygame

dirname = os.path.dirname(__file__)


class Ball(pygame.sprite.Sprite):
    """Class for the ball in the game

    Attributes:
        update: Moves the ball
    """

    def __init__(self, _x=0, _y=0, ball='blueball.png'):
        """Constructor for the class that creates the ball and places
        it on it's starting position.

        Args:
            x (int, optional): Initial x-coordinate. Defaults to 0.
            y (int, optional): Initial y-coordinate. Defaults to 0.
            ball (str, optional): The color of the ball. Defaults to 'blueball.png'.
        """
        super().__init__()
        self.image = pygame.image.load(os.path.join(
            dirname, 'assets/balls', ball))
        self.rect = self.image.get_rect()
        self.rect.x = _x
        self.rect.y = _y
