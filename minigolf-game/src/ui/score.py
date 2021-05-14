import pygame


class Score:
    """A class to show the current score during a game."""

    def __init__(self, display):
        """Initializes a pygame font for the score.

        Args:
            display: The current pygame display for the game.
        """
        self._display = display
        self._font = pygame.font.SysFont('Arial', 18)

    def draw_score(self, score):
        """Draws the score on the display.

        Args:
            score: The current score.
        """
        text = self._font.render(str(score) + ' shots', True, (255, 0, 0))
        self._display.blit(text, (15, 15))
