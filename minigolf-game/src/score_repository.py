from initialize_db import initialize
from db_connection import get_db_connection


class ScoreRepository:
    def __init__(self):
        self._connection = get_db_connection()

    def find_all(self):
        cursor = self._connection.cursor()
        cursor.execute('SELECT * FROM scores ORDER BY level')
        all_scores = cursor.fetchall()
        return all_scores

    def find_all_by_level(self, level):
        cursor = self._connection.cursor()
        command = 'SELECT * FROM scores WHERE level=? ORDER BY score'
        cursor.execute(command, [level])
        all_scores_by_level = cursor.fetchall()
        return all_scores_by_level

    def find_all_by_player(self, player):
        cursor = self._connection.cursor()
        command = 'SELECT * FROM scores WHERE player=? ORDER BY level'
        cursor.execute(command, [player])
        return cursor.fetchall()

    def add_score(self, player, level, score):
        cursor = self._connection.cursor()
        command = 'INSERT INTO scores (player, level, score) VALUES (?, ?, ?)'
        cursor.execute(command, [player, level, score])
        self._connection.commit()

    def print_scores(self):
        scores = self.find_all()
        for score in scores:
            print(f'level: {score[0]}, player: {score[1]}, score: {score[2]}')

    def print_level(self, level):
        scores = self.find_all_by_level(level)
        print(f'Level {level} scores')
        for score in scores:
            print(f'player: {score[1]}, score: {score[2]}')

    def print_player(self, player):
        scores = self.find_all_by_player(player)
        print(f"Player {player}'s scores")
        for score in scores:
            print(f'level: {score[0]}, score: {score[2]}')


if __name__ == '__main__':
    score = ScoreRepository()
    # print(list(score.find_all()[0]))
    score.print_level(2)
    # score.print_player('makeri')
