import sqlite3

DB_NAME = "petto.db"


def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS pets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            species TEXT,
            age INTEGER,
            notes TEXT
        )
        """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS adopters (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT,
            city TEXT,
            experience TEXT
        )
        """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS followups (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pet_id INTEGER,
            adopter_id INTEGER,
            adaptation_score INTEGER,
            notes TEXT
        )
        """
    )

    conn.commit()
    conn.close()


def add_pet(name, species, age, notes):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO pets (name, species, age, notes) VALUES (?, ?, ?, ?)",
        (name, species, age, notes)
    )

    conn.commit()
    conn.close()


def add_adopter(full_name, city, experience):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO adopters (full_name, city, experience) VALUES (?, ?, ?)",
        (full_name, city, experience)
    )

    conn.commit()
    conn.close()


def create_followup(pet_id, adopter_id, adaptation_score, notes):
    return [dict(r) for r in rows]
