import sqlite3

from config import DATABASE_PATH


def get_connection():
    """
    Crea conexión SQLite.

    Returns:
        sqlite3.Connection

    Raises:
        RuntimeError
    """

    try:
        connection = sqlite3.connect(DATABASE_PATH)
        connection.row_factory = sqlite3.Row
        return connection

    except sqlite3.Error as error:
        raise RuntimeError(f"Error conectando DB: {error}")
