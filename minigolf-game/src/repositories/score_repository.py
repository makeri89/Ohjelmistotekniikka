from services.database.db_connection import get_db_connection


class ScoreRepository:
    """A class to save the scores of each game in a database.

    Attributes:
        connection: A database connection using sqlite3
    """

    def __init__(self):
        """A constructor that creates a connection to the database
        """
        self._connection = get_db_connection()

    def find_all(self):
        """A method to find all saved scores from the database.

        Returns:
            sqlite3 object: An iterable object with the database rows from the query
        """
        cursor = self._connection.cursor()
        cursor.execute('SELECT * FROM scores ORDER BY level')
        all_scores = cursor.fetchall()
        return all_scores

    def find_all_by_level(self, level):
        """A method to find all saved scores from the database on a specific level.

        Args:
            level (int): Level number

        Returns:
            sqlite3 object: An iterable object with the database rows from the query
        """
        cursor = self._connection.cursor()
        command = 'SELECT * FROM scores WHERE level=? ORDER BY score'
        cursor.execute(command, [level])
        all_scores_by_level = cursor.fetchall()
        return all_scores_by_level

    def find_all_by_player(self, player):
        """A method to find all scores in the database by a specific player.

        Args:
            player (string): The name of the player

        Returns:
            sqlite3 object: An iterable object with the database rows from the query
        """
        cursor = self._connection.cursor()
        command = 'SELECT * FROM scores WHERE player=? ORDER BY level'
        cursor.execute(command, [player])
        return cursor.fetchall()

    def add_score(self, player, level, score):
        """A method to add new scores to the database.

        A new score is added after every game played.

        Args:
            player (string): The name of the player
            level (int): Level number
            score (int): Shot count
        """
        cursor = self._connection.cursor()
        command = 'INSERT INTO scores (player, level, score) VALUES (?, ?, ?)'
        cursor.execute(command, [player, level, score])
        self._connection.commit()
