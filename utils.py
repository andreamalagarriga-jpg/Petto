def risk_label(score):
    if score <= 3:
        return "ALTO"

    if score <= 6:
        return "MEDIO"

    return "BAJO"
