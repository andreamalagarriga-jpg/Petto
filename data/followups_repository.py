from data.database import get_connection


def create_followup(
    pet_name,
    adopter_name,
    adaptation_score,
    notes
):
    """
    Guarda seguimiento.
    """

    try:
        connection = get_connection()

        connection.execute(
            """
            INSERT INTO followups (
                pet_name,
                adopter_name,
                adaptation_score,
                notes
            ) VALUES (?, ?, ?, ?)
            """,
            (
                pet_name,
                adopter_name,
                adaptation_score,
                notes
            )
        )

        connection.commit()
        connection.close()

    except Exception as error:
        raise RuntimeError(f"Error guardando seguimiento: {error}")


def fetch_all_followups():
    """
    Obtiene seguimientos.
    """

    try:
        connection = get_connection()

        rows = connection.execute(
            "SELECT * FROM followups ORDER BY id DESC"
        ).fetchall()

        connection.close()

        return [dict(row) for row in rows]

    except Exception as error:
        raise RuntimeError(f"Error obteniendo seguimientos: {error}")
