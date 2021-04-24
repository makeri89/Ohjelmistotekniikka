from db_connection import get_db_connection


def create_tables(connection):
    """Creates the database tables needed to save the scores.

    Args:
        connection: A database connection
    """
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE scores (
            level INTEGER,
            player TEXT,
            score INTEGER
        );
    ''')

    connection.commit()


def drop_tables(connection):
    """Clears the database.

    Args:
        connection: A database connection
    """
    cursor = connection.cursor()
    cursor.execute('''
        DROP TABLE IF EXISTS scores;
    ''')
    connection.commit()


def initialize():
    """Initializes the database by creating empty tables.

    Can be used to reset the database also.
    """
    connection = get_db_connection()
    drop_tables(connection)
    create_tables(connection)


if __name__ == '__main__':
    initialize()
