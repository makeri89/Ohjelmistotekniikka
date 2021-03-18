import unittest
from field import Field

field_map = [[1,1,1,1,1],
             [1,2,2,3,1],
             [1,2,2,3,1],
             [1,2,2,2,1],
             [1,2,4,4,1],
             [1,2,4,5,1],
             [1,2,2,0,1],
             [1,1,1,1,1]]

class TestField(unittest.TestCase):
    def setUp(self):
        self.field = Field(field_map)
        
    def test_elements_are_created_correctly(self):
        self.assertEqual(len(self.field.walls), 22)
        self.assertEqual(len(self.field.grass), 11)
        self.assertEqual(len(self.field.holes), 1)
        self.assertEqual(len(self.field.water), 2)
        self.assertEqual(len(self.field.light_sand), 3)
        self.assertEqual(len(self.field.dark_sand), 1)
        
    def test_field_dimensions_correct(self):
        self.assertEqual(self.field.height, len(field_map))
        self.assertEqual(self.field.width, len(field_map[0]))