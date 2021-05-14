import pygame

from ui.score import Score


class Renderer:
    """A class to handle rendering in pygame."""

    def __init__(self, display, field, ball, aim_line):
        """A constuctor that sets the pygame display and the field.

        Args:
            display (pygame display): The display object for the field.
            field (Field): A Field class object containing sprites.
            ball (Ball): The ball sprite that is on the field.
            aim_line (AimLine): The aiming line drawn from the ball.
        """
        self._display = display
        self._field = field
        self._ball = ball
        self._aim_line = aim_line
        self._score = Score(self._display)

    def render(self, score):
        """A method to update all of the sprites on the field.

        Args:
            score: The current amount of shots made.
        """
        self._field.update(self._display)
        self.draw_aim()
        self._score.draw_score(score)
        pygame.display.update()

    def draw_aim(self):
        """A method to draw the aiming line."""
        mouse_pos = pygame.mouse.get_pos()
        current_x, current_y = self._ball.rect.x, self._ball.rect.y
        self._aim_line.draw_line(current_x, current_y, mouse_pos)
