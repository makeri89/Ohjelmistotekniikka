class Walls:
    """A class to get the coordinates for all of the walls in the field.

        The coordinates are grouped to allow proper collision detection
        depending on the direction of the ball.
    """

    def __init__(self, field_map):
        """A constructor that initializes the dicts needed to store
        the walls on the field.

        Calls the methods contact_points and singular_ranges that
        map through the field_map and determine the contact areas
        of the walls on the field into ranges.

        Args:
            field_map: The field as a 2D matrix
        """
        self.__field_map = field_map
        self._walls = {'top': [], 'bottom': [], 'left': [], 'right': []}
        self._wall_ranges = {'top': {}, 'bottom': {}, 'left': {}, 'right': {}}

        self.contact_points()
        self.singular_ranges()

    def contact_points(self):
        """A method to find all groups of walls.

        Every wall gets constructed from single wall pieces in the field
        and put into a dictionary in a way that separates the walls that
        can be hit from below, from above etc.
        """
        for y in range(1, len(self.__field_map)-1):
            for x in range(1, len(self.__field_map[0])-1):
                if self.__field_map[y][x] == 1:
                    if self.__field_map[y-1][x] != 1:
                        self._walls['top'].append((x, y))
                    if self.__field_map[y+1][x] != 1:
                        self._walls['bottom'].append((x, y))
                    if self.__field_map[y][x-1] != 1:
                        self._walls['left'].append((x, y))
                    if self.__field_map[y][x+1] != 1:
                        self._walls['right'].append((x, y))

    def singular_ranges(self):
        """A method to organize the ranges of the walls.

        The ranges are arranged according to their x or y coordinate
        depending on their position.
        """
        walls_on_coordinates = {'top': {},
                                'bottom': {}, 'left': {}, 'right': {}}
        for direction, coordinates in self._walls.items():
            if direction in ('left', 'right'):
                for i in coordinates:
                    if i[0] not in walls_on_coordinates[direction]:
                        walls_on_coordinates[direction][i[0]] = []
                        self._wall_ranges[direction][i[0]] = []
                    walls_on_coordinates[direction][i[0]].append(i[1])
            else:
                for i in coordinates:
                    if i[1] not in walls_on_coordinates[direction]:
                        walls_on_coordinates[direction][i[1]] = []
                        self._wall_ranges[direction][i[1]] = []
                    walls_on_coordinates[direction][i[1]].append(i[0])

        for direction, coordinates in walls_on_coordinates.items():
            for cross_coord, coord_list in coordinates.items():
                self._wall_ranges[direction][cross_coord] = self.get_ranges(
                    coord_list)

    def get_ranges(self, coord_list):
        """A method to find all the ranges from a list.

        Args:
            coord_list: List of coordinates for walls
                        in the field at certain x or y coordinate.

        Returns:
            list: A list of all the ranges as tuples.
        """
        length = len(coord_list)
        ranges = []
        current = [coord_list[0]]
        for i in range(1, length):
            if coord_list[i]-1 == coord_list[i-1]:
                current.append(coord_list[i])
            else:
                ranges.append((current[0], current[-1]+1))
                current = [coord_list[i]]
        ranges.append((current[0], current[-1]+1))
        return ranges

    def get_contact_points(self):
        """A method to access the ranges from outside of the class.

        Returns:
            list: A list of ranges for all walls in the field.
        """
        return self._wall_ranges
