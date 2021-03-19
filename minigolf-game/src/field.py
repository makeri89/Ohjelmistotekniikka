import pygame
from element import Element
from ball import Ball


class Field:
    """A class for creating the field.

    Attributes:
        height, width: Dimensions of the current field
        holes,
        walls,
        grass,
        water,
        light_sand,
        dark_sand: Groups of sprite objects in the field
        all_elements: A combined group of all of the other sprite groups
        ball: A sprite object for the ball
    """

    def __init__(self, field_map):
        """Constructor that creates sprite groups
        for all the different elements on the field.

        Args:
            field_map: The map of the field as a matrix where different
            values correspond to different elements.
        """
        self.__cell_size = 15
        self._height = len(field_map)
        self._width = len(field_map[0])
        self._holes = pygame.sprite.Group()
        self._walls = pygame.sprite.Group()
        self._grass = pygame.sprite.Group()
        self._water = pygame.sprite.Group()
        self._light_sand = pygame.sprite.Group()
        self._dark_sand = pygame.sprite.Group()
        self._all_elements = pygame.sprite.Group()
        self._ball = None

        self.place_elements(field_map)

    def place_elements(self, field_map):
        """Method to place all the elements in their correct location based on the map

        Args:
            field_map: Locations for the elements
        """
        for y_coord in range(self._height):
            for x_coord in range(self._width):
                cell = field_map[y_coord][x_coord]
                norm_x = x_coord * self.__cell_size
                norm_y = y_coord * self.__cell_size

                if cell == 0:
                    self._holes.add(Element(norm_x, norm_y, 0))
                elif cell == 1:
                    self._walls.add(Element(norm_x, norm_y, 1))
                elif cell == 2:
                    self._grass.add(Element(norm_x, norm_y, 2))
                elif cell == 3:
                    self._water.add(Element(norm_x, norm_y, 3))
                elif cell == 4:
                    self._light_sand.add(Element(norm_x, norm_y, 4))
                elif cell == 5:
                    self._dark_sand.add(Element(norm_x, norm_y, 5))
                elif cell == 6:
                    self._ball = Ball(norm_x, norm_y)
                    self._grass.add(Element(norm_x, norm_y, 2))

        self._all_elements.add(self._holes, self._walls, self._water,
                               self._grass, self._light_sand, self._dark_sand, self._ball)

    def get_ball(self):
        """A method to access to the ball from outside of the class

        Returns:
            Ball: The ball sprite object
        """
        return self._ball
    
    def get_holes(self):
        return self._holes

    def update(self, display):
        """Updates all sprites in the class

        Args:
            display: The current pygame screen
        """
        self._all_elements.update(display)

    def check_wall_hits(self):
        """Checks if the ball has hit the wall

        Returns:
            If there is contact, it returns the ball, else None.
        """
        contact = pygame.sprite.spritecollide(self._ball, self._walls, dokill=False)
        return contact

    def check_water_hits(self):
        """Checks if the ball has gone to water

        Returns:
            If there is contact, it returns the ball, else None.
        """
        contact = pygame.sprite.spritecollideany(self._ball, self._water)
        return contact
    
    # def in_hole(self):
    #     """A method to check if the hole ands the ball are colliding.

    #     Uses a circle ratio instead of the default rectangle.
    #     """
    #     in_hole = pygame.sprite.spritecollide(
    #         self._ball, self._holes, False, pygame.sprite.collide_circle_ratio(0.3))
    #     if in_hole:
    #         print('you won')
    #         pygame.quit()
