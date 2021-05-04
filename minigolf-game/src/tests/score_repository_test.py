import unittest
import pytest

from initialize_db import initialize as init_db
from repositories.score_repository import ScoreRepository


@pytest.mark.nonvisual
class TestScoreRepository(unittest.TestCase):
    def setUp(self):
        init_db()
        self.repository = ScoreRepository()

    def add_scores(self):
        self.repository.add_score('tester1', 1, 5)
        self.repository.add_score('tester1', 2, 4)
        self.repository.add_score('tester2', 1, 3)

    def test_add_score(self):
        self.add_scores()
        scores = self.repository.find_all()
        self.assertEqual(len(scores), 3)
        self.assertEqual(scores[0][0], 1)

    def test_find_all(self):
        self.add_scores()
        scores = self.repository.find_all()
        self.assertEqual(len(scores), 3)
        self.assertEqual(scores[0][1], 'tester1')
        self.assertEqual(scores[1][1], 'tester2')
        self.assertEqual(scores[1][0], 1)
        self.assertEqual(scores[1][2], 3)
        self.assertEqual(scores[2][0], 2)

    def test_find_all_by_level(self):
        self.add_scores()
        level_1_scores = self.repository.find_all_by_level(1)
        level_2_scores = self.repository.find_all_by_level(2)
        self.assertEqual(len(level_1_scores), 2)
        self.assertEqual(level_1_scores[0][2], 3)
        self.assertEqual(level_1_scores[0][1], 'tester2')
        self.assertEqual(level_1_scores[1][2], 5)
        self.assertEqual(len(level_2_scores), 1)

    def test_find_all_by_player(self):
        self.add_scores()
        player_1_scores = self.repository.find_all_by_player('tester1')
        player_2_scores = self.repository.find_all_by_player('tester2')
        self.assertEqual(len(player_1_scores), 2)
        self.assertEqual(len(player_2_scores), 1)
        self.assertEqual(player_1_scores[0][0], 1)
        self.assertEqual(player_1_scores[1][0], 2)
