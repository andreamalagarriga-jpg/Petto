from data.database import get_connection


def create_adopter(full_name, city, experience):
    """
    Guarda adoptante.
    """

    try:
        connection = get_connection()

        connection.execute(
            """
            INSERT INTO adopters (
                full_name,
                city,
                experience
            ) VALUES (?, ?, ?)
            """,
            (full_name, city, experience)
        )

        connection.commit()
        connection.close()

    except Exception as error:
        raise RuntimeError(f"Error guardando adoptante: {error}")


def fetch_all_adopters():
    """
    Obtiene adoptantes.
    """

    try:
        connection = get_connection()

        rows = connection.execute(
            "SELECT * FROM adopters ORDER BY id DESC"
        ).fetchall()

        connection.close()

        return [dict(row) for row in rows]

    except Exception as error:
        raise RuntimeError(f"Error obteniendo adoptantes: {error}")
