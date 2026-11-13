def HPI_final_score(linguistic_component: float, computing_component: float) -> float:
    """
    Calculates the final ordinary grade for 'Habilidades Profesionales para Ingenieros'
    as a single float.
    """
    if linguistic_component >= 5 and computing_component >= 5.0:
        final_score: float = (0.30 * linguistic_component) + (0.70 * computing_component)
        return round(final_score, 2)
    else:
        return 0.0