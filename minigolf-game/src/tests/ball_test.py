import unittest
import pytest
from field_elements.ball import Ball


@pytest.mark.nonvisual
class TestBall(unittest.TestCase):
    def setUp(self):
        self.ball = Ball(10, 10)

    def test_ball_coordinates_are_set_correctly(self):
        self.assertEqual((self.ball.rect.x, self.ball.rect.y), (10, 10))

    def test_ball_moves_correctly(self):
        self.ball.rect.move_ip(10, -5)
        self.assertEqual((self.ball.rect.x, self.ball.rect.y), (20, 5))
