import os

import pygame

dirname = os.path.dirname(__file__)

balls = {'blue': 'blueball.png', 'green': 'greenball.png',
         'yellow': 'yellowball.png', 'red': 'redball.png'}


class Ball(pygame.sprite.Sprite):
    """Class for the ball in the game

    Attributes:
        image: The image loaded from a file
        rect: Pygame rect object from the image
    """

    def __init__(self, _x=0, _y=0, ball='blue'):
        """Constructor for the class that creates the ball and places
        it on it's starting position.

        Args:
            x (int, optional): Initial x-coordinate. Defaults to 0.
            y (int, optional): Initial y-coordinate. Defaults to 0.
            ball (str, optional): The color of the ball. Defaults to 'blueball.png'.
        """
        super().__init__()
        self.image = pygame.image.load(os.path.join(
            dirname, '../assets/balls', balls[ball]))
        self.rect = self.image.get_rect()
        self.rect.x = _x
        self.rect.y = _y

    def move(self, x=0, y=0):
        """Moves the ball with the move_ip method of pygame rect object

        Args:
            x (int, optional): The moving distance on x coordinates. Defaults to 0.
            y (int, optional): The moving distance on y coordinates. Defaults to 0.
        """
        self.rect.move_ip(x, y)

    def get_coordinates(self):
        return self.rect.x, self.rect.y

    def set_location(self, x, y):
        self.rect.x = x
        self.rect.y = y
