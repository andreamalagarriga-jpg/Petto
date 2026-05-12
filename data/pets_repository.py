from data.database import get_connection


def create_pet(name, species, age, notes):
    """
    Guarda mascota.
    """

    try:
        connection = get_connection()

        connection.execute(
            """
            INSERT INTO pets (
                name,
                species,
                age,
                notes
            ) VALUES (?, ?, ?, ?)
            """,
            (
                name,
                species,
                age,
                notes
            )
        )

        connection.commit()
        connection.close()

        return True, "Mascota registrada correctamente."

    except Exception as error:
        return False, f"Error guardando mascota: {error}"


def fetch_all_pets():
    """
    Obtiene mascotas.
    """

    try:
        connection = get_connection()

        rows = connection.execute(
            "SELECT * FROM pets ORDER BY id DESC"
        ).fetchall()

        connection.close()

        return [dict(row) for row in rows]

    except Exception:
        return []
