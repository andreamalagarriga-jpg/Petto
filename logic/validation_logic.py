def validate_required_text(value, field_name):
    """
    Valida texto requerido.
    """

    if not value:
        return False, f"{field_name} es obligatorio."

    if not value.strip():
        return False, f"{field_name} no puede estar vacío."

    return True, ""


def validate_positive_number(value, field_name):
    """
    Valida números positivos.
    """

    if value < 0:
        return False, f"{field_name} debe ser positivo."

    return True, ""
