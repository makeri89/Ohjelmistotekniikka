from db_connection import get_db_connection


def create_tables(connection):
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
    cursor = connection.cursor()
    cursor.execute('''
        DROP TABLE IF EXISTS scores;
    ''')
    connection.commit()


def initialize():
    connection = get_db_connection()
    drop_tables(connection)
    create_tables(connection)


if __name__ == '__main__':
    initialize()
