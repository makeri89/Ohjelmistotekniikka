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
            
        # print(self.find_walls())

        self.contact_points()

    def contact_points(self):
        """A method to find all groups of walls.

        Every wall gets constructed from single wall pieces in the field
        and put into a dictionary in a way that separates the walls that
        can be hit from below, from above etc. The length of each wall
        is saved as a range from the first wall piece to the last wall piece.
        """
        walls_on_coordinates = {'top': {}, 'bottom': {}, 'left': {}, 'right': {}}
        
        for y in range(1,len(self.__field_map)-1):
            for x in range(1,len(self.__field_map[0])-1):
                if self.__field_map[y][x] == 1:
                    if self.__field_map[y-1][x] != 1:
                        self._walls['top'].append((x,y))
                    if self.__field_map[y+1][x] != 1:
                        self._walls['bottom'].append((x,y))
                    if self.__field_map[y][x-1] != 1:
                        self._walls['left'].append((x,y))
                    if self.__field_map[y][x+1] != 1:
                        self._walls['right'].append((x,y))
                        
        for k, v in self._walls.items():
            if k == 'left' or k == 'right':
                for i in v:
                    if i[0] not in walls_on_coordinates[k]:
                        walls_on_coordinates[k][i[0]] = []
                    walls_on_coordinates[k][i[0]].append(i[1])
            else:
                for i in v:
                    if i[1] not in walls_on_coordinates[k]:
                        walls_on_coordinates[k][i[1]] = []
                    walls_on_coordinates[k][i[1]].append(i[0])
                
        print(walls_on_coordinates)
            
            

    def get_contact_points(self):
        return self._walls
