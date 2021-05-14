import time

import pygame


class EndScreen:
    """A class to display information after a game is played."""

    def __init__(self):
        """Sets a new pygame display and fonts."""
        pygame.init()
        self._display = pygame.display.set_mode((600, 250))
        self._display.fill((153, 255, 153))
        self._title_font = pygame.font.SysFont('Arial', 42)
        self._regular_font = pygame.font.SysFont('Arial', 26)
        self._small_font = pygame.font.SysFont('Arial', 18)

    def draw_endscreen(self, score):
        """A method that draws the information about the game just played.

        Displays a real time timer when returning to the main menu.

        Args:
            score (int): The amount of shots needed on the last game
        """
        for i in range(5, 0, -1):
            self._display.fill((153, 255, 153))
            won_text = self._title_font.render(
                'You finished the level!', True, (224, 144, 144))
            score_text = self._regular_font.render(
                'You needed ' + str(score) + ' shots', True, (64, 128, 64))
            self._display.blit(won_text, (110, 60))
            self._display.blit(score_text, (190, 130))
            return_text = self._small_font.render(
                'Returning to main menu in ' + str(i) + ' seconds...', True, (64, 128, 64))
            self._display.blit(return_text, (155, 200))
            pygame.display.update()
            time.sleep(1)
        pygame.quit()
