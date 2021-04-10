import pygame


class Score:
    def __init__(self, display):
        self.display = display
        self.font = pygame.font.SysFont('Arial', 18)

    def draw_score(self, score):
        text = self.font.render(str(score) + ' shots', True, (255, 0, 0))
        self.display.blit(text, (15, 15))
