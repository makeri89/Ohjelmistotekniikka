import unittest
import pytest

from services.ball_handler import BallHandler
from services.shot_counter import ShotCounter


class MockBall:
    def __init__(self):
        self.x = 20
        self.y = 20

    def move(self, x, y):
        self.x += x
        self.y += y

    def get_coordinates(self):
        return self.x, self.y

    def set_location(self, x, y):
        self.x = x
        self.y = y


class MockField:
    def check_water_hits(self, helper):
        return helper

    def get_dimensions(self):
        return 200, 300

    def in_hole(self):
        pass


mock_hit_ranges = {'right': {}, 'left': {}, 'top': {}, 'bottom': {}}


@pytest.mark.nonvisual
class TestBallHandler(unittest.TestCase):
    def setUp(self):
        self.ball = MockBall()
        self.field = MockField()
        self.shot_counter = ShotCounter()
        self.ball_handler = BallHandler(
            self.ball, self.field, mock_hit_ranges, self.shot_counter)

    def test_everything_set_up_correctly(self):
        self.assertEqual(self.ball_handler.ball.get_coordinates(),
                         self.ball.get_coordinates())
        self.assertEqual(self.ball_handler.field.get_dimensions(),
                         self.field.get_dimensions())
        self.assertEqual(self.ball_handler.counter.get_shots(),
                         self.shot_counter.get_shots())

    def test_shot_is_handled_correctly(self):
        self.ball_handler.handle_shot((100, 100))
        self.assertEqual(self.ball_handler.x_dir, 74)
        self.assertEqual(self.ball_handler.y_dir, 74)
        self.assertEqual(int(self.ball_handler.shot_power), 209)
        self.assertEqual(self.shot_counter.get_shots(), 1)
        self.assertEqual(self.ball_handler.velocity, 100)

    def test_rolling_ball_cannot_be_hit(self):
        self.ball_handler.handle_shot((100, 100))
        self.assertEqual(self.ball_handler.x_dir, 74)
        self.assertEqual(self.ball_handler.y_dir, 74)
        self.assertEqual(self.shot_counter.get_shots(), 1)
        self.ball_handler.handle_shot((0, 0))
        self.assertEqual(self.ball_handler.x_dir, 74)
        self.assertEqual(self.ball_handler.y_dir, 74)
        self.assertEqual(self.shot_counter.get_shots(), 1)

    def test_ball_moves_correctly(self):
        self.ball_handler.handle_shot((126, 126))
        self.assertEqual(self.ball_handler.x_dir, 100)
        self.assertEqual(self.ball_handler.y_dir, 100)
        self.ball_handler.move_ball()
        self.assertEqual(self.ball.get_coordinates(), (21, 21))

    def test_ball_stops_when_it_has_moved_far_enough(self):
        self.ball_handler.handle_shot((100, 100))
        self.ball_handler.move_ball()
        self.assertNotEqual(self.ball_handler.x_dir, 0)
        self.assertEqual(self.ball_handler.shot_allowed, False)
        self.ball_handler.total_trip = 300
        self.ball_handler.move_ball()
        self.assertEqual(self.ball_handler.x_dir, 0)
        self.assertEqual(self.ball_handler.shot_allowed, True)

    def test_hitting_water_resets_the_ball(self):
        self.ball_handler.handle_shot((126, 126))
        self.ball_handler.move_ball()
        self.ball_handler.move_ball()
        self.ball_handler.move_ball()
        self.ball_handler.move_ball()
        self.ball_handler.move_ball()
        self.assertEqual(self.ball.get_coordinates(), (25, 25))
        self.ball_handler.water_hit(True)
        self.assertEqual(self.ball.get_coordinates(), (20, 20))

    def test_outer_wall_horizontal_hits_are_handled_correctly(self):
        self.ball_handler.x_dir = -1
        self.ball_handler.check_outer_walls(15, 20)
        self.assertEqual(self.ball_handler.x_dir, 1)
        self.ball_handler.check_outer_walls(272, 20)
        self.assertEqual(self.ball_handler.x_dir, -1)

    def test_outer_wall_vertical_hits_are_handled_correctly(self):
        self.ball_handler.y_dir = -1
        self.ball_handler.check_outer_walls(20, 15)
        self.assertEqual(self.ball_handler.y_dir, 1)
        self.ball_handler.check_outer_walls(20, 172)
        self.assertEqual(self.ball_handler.y_dir, -1)
