import os

import pygame

dirname = os.path.dirname(__file__)

element_images = {0: 'hole.png', 1: 'wall.png', 2: 'grass.png', 3: 'water.png',
                  4: 'lightsand.png', 5: 'darksand.png'}


class Element(pygame.sprite.Sprite):
    """
    A class for different elements on the field.

    Attributes:
        image: The image loaded from a file
        rect: Pygame rect object from the image
    """

    def __init__(self, _x=0, _y=0, elem=2):
        """Constructor that places the elements on the field.

        Args:
            _x (int, optional): x-coordinate. Defaults to 0.
            _y (int, optional): y-coordinate. Defaults to 0.
            elem (int, optional): Tells the class which element it is supposed to be.
                                  Defaults to grass.
        """
        super().__init__()
        self.path = os.path.join(
            dirname, '../assets/field', element_images[elem])
        self.image = pygame.image.load(self.path)
        self.rect = self.image.get_rect()
        self.rect.x = _x
        self.rect.y = _y
