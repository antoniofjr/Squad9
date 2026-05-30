def calculate_risk(issues):

    score = len(issues) * 2

    if score >= 8:
        level = "CRÍTICO"
    elif score >= 4:
        level = "ALTO"
    else:
        level = "BAIXO"

    return {
        "score": score,
        "level": level
    }