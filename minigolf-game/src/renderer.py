import pygame


class Renderer:
    """A class to handle rendering in pygame.
    """
    def __init__(self, display, field):
        """A constuctor that sets the pygame display and the field.

        Args:
            display: Pygame display
            field: A Field class object containing sprites
        """
        self._display = display
        self._field = field

    def render(self):
        """A method to update all of the sprites on the field.
        """
        self._field.update(self._display)
        pygame.display.update()
