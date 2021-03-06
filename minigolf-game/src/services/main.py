import pygame

from entities.field import Field
from entities.aim_line import AimLine
from levels.field_importer import get_field
from services.ball_handler import BallHandler
from services.shot_counter import ShotCounter
from services.renderer import Renderer
from services.game import Game
from services.clock import Clock
from services.walls import Walls
from repositories.score_repository import ScoreRepository
from ui.end_screen import EndScreen

CELL_SIZE = 15


def main(name='Player 1', level=4, ball_color='blue'):
    """The main function to launch the game.

    Initializes pygame, sets the display dimensions
    and initializes all the objects needed to run the game.
    When the game ends successfully, the score is saved
    and a winning end screen is displayed for 5 seconds.

    Args:
        name (str, optional):
            The name the player enters in the menu.
            Defaults to 'Player 1'.
        level (int, optional):
            The level number the player chose. Defaults to 2.
        ball_color (str, optional):
            The ball color the player chose. Defaults to 'blue'.
    """
    field_map = get_field(int(level))
    height = len(field_map)
    width = len(field_map[0])

    # TkInter passes an empty string as name if name is not given
    if name == '':
        name = 'Player 1'

    pygame.init()

    pygame.display.set_caption(f'{name} is now playing')

    display = pygame.display.set_mode((width*CELL_SIZE, height*CELL_SIZE))
    field = Field(field_map, ball_color)
    walls = Walls(field_map)
    clock = Clock()
    ball = field.get_ball()
    aim_line = AimLine(display)
    counter = ShotCounter()
    ball_handler = BallHandler(
        ball, field, walls.get_contact_points(), counter)
    renderer = Renderer(display, field, ball, aim_line)

    score_repository = ScoreRepository()

    game = Game(clock, display, renderer, ball_handler, counter, field)
    game.run()

    if game.finished:
        score = counter.get_shots()
        score_repository.add_score(name, level, score)
        end_screen = EndScreen()
        end_screen.draw_endscreen(score)


if __name__ == '__main__':
    main()
