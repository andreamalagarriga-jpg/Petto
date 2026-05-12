def validate_required_text(value, field_name):
    """
    Valida texto requerido.

    Inputs:
        value (str)
        field_name (str)

    Returns:
        tuple(bool, str)
    """

    if not value or not value.strip():
        return False, f"{field_name} es obligatorio"

    return True, ""
