import os
from tkinter import Tk
import pygame
from field_elements.field import Field
from clock import Clock
from game import Game
from renderer import Renderer
from ball_handler import BallHandler
from levels.field_two import get_field
from field_elements.aim_line import AimLine
from ui.menu import Menu

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

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
    ball = field.get_ball()
    aim_line = AimLine(display)
    ball_handler = BallHandler(ball, field, aim_line)
    renderer = Renderer(display, field, ball, aim_line)

    game = Game(clock, field, display, renderer, ball_handler)
    game.run()

# window = Tk()
# window.title('Main menu')
# window['bg'] = '#13a713'

# ui = Menu(window, main)
# ui.start()


if __name__ == '__main__':
    # window.mainloop()
    main()
