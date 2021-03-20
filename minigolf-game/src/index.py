import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from field import Field
from clock import Clock
from game import Game
from renderer import Renderer
from ball_handler import BallHandler
from field_two import get_field

CELL_SIZE = 15


def main():
    """The main function to launch the game.

    Initializes pygame, sets the display dimensions
    and initializes the field and the clock objects needed
    to run the game.
    """
    field_map = get_field()
    height = len(field_map)
    width = len(field_map[0])
    
    pygame.init()

    display = pygame.display.set_mode((width*CELL_SIZE, height*CELL_SIZE))
    field = Field(field_map)
    clock = Clock()
    renderer = Renderer(display, field)
    ball = field.get_ball()
    ball_handler = BallHandler(ball, field)

    game = Game(clock, field, display, renderer, ball_handler)
    game.run()

if __name__ == '__main__':
    main()
