from config import LOW_RISK_MIN, MEDIUM_RISK_MIN


def calculate_risk_label(score):
    """
    Calcula nivel de riesgo.

    Inputs:
        score (int)

    Returns:
        str
    """

    if score >= LOW_RISK_MIN:
        return "BAJO"

    if score >= MEDIUM_RISK_MIN:
        return "MEDIO"

    return "ALTO"
