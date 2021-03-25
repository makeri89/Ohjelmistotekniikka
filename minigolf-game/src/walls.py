import pygame


class Walls:
    def __init__(self, field_map):
        """A class to get the coordinates for all of the walls in the field:

        The coordinates are grouped to allow proper collision detection
        depending on the direction of the ball.

        Args:
            field_map: The field as a 2D matrix
        """
        self.__field_map = field_map
        self._walls = {'top': [], 'bottom': [], 'left': [], 'right': []}
        
        # for i in field_map:
        #     print(i)
            
        print(self.find_walls())

        self.contact_points()

    def contact_points(self):
        """A method to find all groups of walls.

        Every wall gets constructed from single wall pieces in the field
        and put into a dictionary in a way that separates the walls that
        can be hit from below, from above etc. The length of each wall
        is saved as a range from the first wall piece to the last wall piece.
        """
        for y in range(len(self.__field_map)):
            for x in range(len(self.__field_map[0])):
                if self.__field_map[y][x] == 1:
                    if self.__field_map[y-1][x] != 1:
                        self._walls['top'].append(x,y)
                    if self.__field_map[y+1][x] != 1:
                        self._walls['bottom'].append(x,y)
                    if self.__field_map[y][x-1] != 1:
                        self._walls['left'].append(x,y)
                    if self.__field_map[y][x+1] != 1:
                        self._walls['right'].append((x,y))
        
        
        # top = bottom = left = right = False
        # start_top = start_bottom = start_right = 0
        # start_left = (0, 0)
        
        # for y in range(1,len(self.__field_map)-1):
        #     for x in range(1,len(self.__field_map[0])-1):
        #         if self.__field_map[y][x] == 1:

        #             if self.__field_map[y+1][x] != 1:
        #                 if not bottom:
        #                     start_bottom = x
        #                     bottom = True
        #             else:
        #                 if bottom:
        #                     bottom = False
        #                     self._walls['bottom'].append((start_bottom, x, y))

        #             if self.__field_map[y-1][x] != 1:
        #                 if not top:
        #                     start_top = x
        #                     top = True
        #             else:
        #                 if top:
        #                     top = False
        #                     self._walls['top'].append((start_top, x, y-1))

        #             if self.__field_map[y][x+1] != 1:
        #                 if not right:
        #                     right = True
        #                     start_right = y
                    # else:
                    #     if right:
                    #         right = False
                    #         self._walls['right'].append((x, start_right, y))

                #     if self.__field_map[y][x-1] != 1:
                #         if not left:
                #             left = True
                #             start_left = (x, y)
                #     # else:
                #     #     if left:
                #     #         left = False
                #     #         self._walls['left'].append((x, start_left[1], y))
                # else:
                #     if bottom:
                #         bottom = False
                #         self._walls['bottom'].append((start_bottom, x, y))

                #     if top:
                #         top = False
                #         self._walls['top'].append((start_top, x, y-1))

                #     if (right and self.__field_map[y+1][x-1] != 1 and self.__field_map[y][x-1] == 1) or (right and self.__field_map[y+1][x-1] != 1 and self.__field_map[y+1][x] == 1):
                #         right = False
                #         self._walls['right'].append((x, start_right, y))

                #     if (left and self.__field_map[y+1][start_left[0]] != 1) or (left and self.__field_map[y+1][start_left[0]] != 1 and self.__field_map[y+1][start_left[0]-1] != 1):
                #         left = False
                #         self._walls['left'].append((start_left[0], start_left[1], y))

        # if bottom:
        #     bottom = False
        #     self._walls['bottom'].append((start_bottom, x, y))

        # if top:
        #     top = False
        #     self._walls['top'].append((start_top, x, y-1))

        # if right:
        #     right = False
        #     self._walls['right'].append((x, start_right, y))

        # if left:
        #     left = False
        #     self._walls['left'].append((start_left[0], start_left[1], y))

    def get_contact_points(self):
        for k, v in self._walls.items():
            print(k, v)
        return self._walls
