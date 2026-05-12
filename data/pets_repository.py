from data.database import get_connection


def create_pet(name, species, age, notes):
    """
    Guarda mascota.

    Returns:
        None
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
            (name, species, age, notes)
        )

        connection.commit()
        connection.close()

    except Exception as error:
        raise RuntimeError(f"Error guardando mascota: {error}")


def fetch_all_pets():
    """
    Obtiene mascotas.

    Returns:
        list[dict]
    """

    try:
        connection = get_connection()

        rows = connection.execute(
            "SELECT * FROM pets ORDER BY id DESC"
        ).fetchall()

        connection.close()

        return [dict(row) for row in rows]

    except Exception as error:
        raise RuntimeError(f"Error obteniendo mascotas: {error}")
