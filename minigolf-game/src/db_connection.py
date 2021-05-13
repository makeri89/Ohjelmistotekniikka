import sqlite3

from config import DB_PATH

connection = sqlite3.connect(DB_PATH)
connection.row_factory = sqlite3.Row


def get_db_connection():
    return connection
