import unittest
from field_elements.element import Element


class TestElement(unittest.TestCase):
    def setUp(self):
        self.hole = Element(elem=0)
        self.wall = Element(elem=1)
        self.grass = Element(elem=2)
        self.water = Element(elem=3)
        self.light_sand = Element(elem=4)
        self.dark_sand = Element(elem=5)

    def test_element_path_is_correct(self):
        self.assertEqual(self.hole.path.split('/')[-1], 'hole.png')
        self.assertEqual(self.wall.path.split('/')[-1], 'wall.png')
        self.assertEqual(self.grass.path.split('/')[-1], 'grass.png')
        self.assertEqual(self.water.path.split('/')[-1], 'water.png')
        self.assertEqual(self.light_sand.path.split('/')[-1], 'lightsand.png')
        self.assertEqual(self.dark_sand.path.split('/')[-1], 'darksand.png')
