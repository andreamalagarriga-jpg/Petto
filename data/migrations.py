from data.database import get_connection


def initialize_database():
    """
    Crea tablas iniciales.

    Raises:
        RuntimeError
    """

    try:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS pets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            species TEXT NOT NULL,
            age INTEGER NOT NULL,
            notes TEXT
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS adopters (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT NOT NULL,
            city TEXT NOT NULL,
            experience TEXT NOT NULL
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS followups (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pet_name TEXT NOT NULL,
            adopter_name TEXT NOT NULL,
            adaptation_score INTEGER NOT NULL,
            notes TEXT
        )
        """)

        connection.commit()
        connection.close()

    except Exception as error:
        raise RuntimeError(f"Error creando tablas: {error}")
