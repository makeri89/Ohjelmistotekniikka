import pygame


class Renderer:
    def __init__(self, display, field, ball):
        self.display = display
        self.field = field
        self.ball = ball
        
    def render(self):
        self.field.all_elements.draw(self.display)
        self.ball.draw(self.display)
        pygame.display.update()