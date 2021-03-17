import pygame
from element import Element


class Field:
    """A class for creating the field

    Attributes:
        place_elements: A method to place the elements on the map.
    """

    def __init__(self, field_map):
        """Constructor that creates sprite groups
        for all the different elements on the field.

        Args:
            field_map: The map of the field as a matrix where different
            values correspond to different elements.
        """
        self.cell_size = 15
        self.height = len(field_map)
        self.width = len(field_map[0])
        self.holes = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.grass = pygame.sprite.Group()
        self.water = pygame.sprite.Group()
        self.light_sand = pygame.sprite.Group()
        self.dark_sand = pygame.sprite.Group()
        self.all_elements = pygame.sprite.Group()

        self.place_elements(field_map)

    def place_elements(self, field_map):
        """Method to place all the elements in their correct location based on the map

        Args:
            field_map: Locations for the elements
        """
        for y_coord in range(self.height):
            for x_coord in range(self.width):
                cell = field_map[y_coord][x_coord]
                norm_x = x_coord * self.cell_size
                norm_y = y_coord * self.cell_size

                if cell == 0:
                    self.holes.add(Element(norm_x, norm_y, 0))
                elif cell == 1:
                    self.walls.add(Element(norm_x, norm_y, 1))
                elif cell == 2:
                    self.grass.add(Element(norm_x, norm_y, 2))
                elif cell == 3:
                    self.water.add(Element(norm_x, norm_y, 3))
                elif cell == 4:
                    self.light_sand.add(Element(norm_x, norm_y, 4))
                elif cell == 5:
                    self.dark_sand.add(Element(norm_x, norm_y, 5))

        self.all_elements.add(self.holes, self.walls, self.water,
                              self.grass, self.light_sand, self.dark_sand)
