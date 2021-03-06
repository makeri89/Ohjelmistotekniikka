import pygame


class AimLine:
    """A class to draw a line to help aiming the ball.

    Attributes:
        line: A pygame line object.
    """

    def __init__(self, display):
        """A constructor that defines the line color
        and the display for the class.

        Args:
            display: Pygame display for the current game
        """
        self.__display = display
        self.__color = (128, 0, 32)
        self.line = None

    def draw_line(self, start_x, start_y, target):
        """A method to draw the line.

        Adding 6 to the coordinates moves the line to
        the center of the ball.

        Args:
            start_x: Starting x coordinate of the line
            start_y: Starting y coordinate of the line
            target: Mouse position
        """
        start = (start_x+6, start_y+6)
        self.line = pygame.draw.line(
            self.__display, self.__color, start, target, 1)
