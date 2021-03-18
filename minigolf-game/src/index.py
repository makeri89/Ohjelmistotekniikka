import pygame
from field import Field
from ball import Ball
from clock import Clock
from game import Game
from field_two import get_field

CELL_SIZE = 15


def main():
    field_map = get_field()
    height = len(field_map)
    width = len(field_map[0])

    pygame.init()

    display = pygame.display.set_mode((width*CELL_SIZE, height*CELL_SIZE))
    field = Field(field_map)
    ball = Ball(6*CELL_SIZE, 10*CELL_SIZE)
    clock = Clock()

    game = Game(ball, clock, field, display)
    game.run()

if __name__ == '__main__':
    main()
