import os
import pygame

dirname = os.path.dirname(__file__)


class Wall(pygame.sprite.Sprite):
    """
    A class for walls in the game.
    """

    def __init__(self, _x=0, _y=0):
        """Constructor that gets the walls coordinates and places it there.

        Args:
            _x (int, optional): x-coordinate. Defaults to 0.
            _y (int, optional): y-coordinate. Defaults to 0.
        """
        super().__init__()
        self.image = pygame.image.load(
            os.path.join(dirname, '../../assets/field', 'wall.png'))
        self.rect = self.image.get_rect()
        self.rect.x = _x
        self.rect.y = _y
