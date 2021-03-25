import unittest
import pygame
from field_elements.aim_line import AimLine


class TestAimline(unittest.TestCase):
    def setUp(self):
        self.display = pygame.display.set_mode((300, 400))
        self.line = AimLine(self.display)

    def test_line_coordinates_are_correct(self):
        self.line.draw_line(10, 30, (100, 200))
        self.assertEqual(self.line.line[0], 10)
        self.assertEqual(self.line.line[1], 30)
        self.assertEqual(self.line.line[2], 100-10+1)
        self.assertEqual(self.line.line[3], 200-30+1)
