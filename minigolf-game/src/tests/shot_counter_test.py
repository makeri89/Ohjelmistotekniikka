import unittest
import pytest

from services.shot_counter import ShotCounter


@pytest.mark.nonvisual
class TestShotCounter(unittest.TestCase):
    def setUp(self):
        self.counter = ShotCounter()

    def test_counter_initializes_to_zero(self):
        self.assertEqual(self.counter.get_shots(), 0)

    def test_making_a_shot_raises_the_counter_value_correctly(self):
        self.counter.plus_one()
        self.assertEqual(self.counter.get_shots(), 1)
        self.counter.plus_one()
        self.counter.plus_one()
        self.assertEqual(self.counter.get_shots(), 3)

    def test_counter_resets_correctly(self):
        self.counter.plus_one()
        self.assertEqual(self.counter.get_shots(), 1)
        self.counter.reset()
        self.assertEqual(self.counter.get_shots(), 0)
