import unittest
import pytest

from services.walls import Walls

field_map = [[1, 1, 1, 1, 1, 1, 1, 1],
             [1, 2, 2, 2, 1, 2, 2, 1],
             [1, 2, 2, 2, 1, 1, 1, 1],
             [1, 2, 2, 2, 1, 2, 2, 1],
             [1, 2, 2, 2, 1, 2, 2, 1],
             [1, 2, 1, 2, 2, 2, 2, 1],
             [1, 2, 1, 2, 2, 2, 2, 1],
             [1, 1, 1, 1, 1, 1, 1, 1]]


@pytest.mark.nonvisual
class TestWalls(unittest.TestCase):
    def setUp(self):
        self.walls = Walls(field_map)

    def test_walls_are_found_correctly(self):
        walls = self.walls.get_contact_points()
        top = walls['top']
        bottom = walls['bottom']
        left = walls['left']
        right = walls['right']
        self.assertEqual(top, {2: [(5, 7)], 5: [(2, 3)]})
        self.assertEqual(bottom, {2: [(5, 7)], 4: [(4, 5)]})
        self.assertEqual(left, {2: [(5, 7)], 4: [(1, 5)]})
        self.assertEqual(right, {2: [(5, 7)], 4: [(1, 2), (3, 5)]})
