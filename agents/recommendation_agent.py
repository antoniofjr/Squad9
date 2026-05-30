def generate_recommendations(issues):

    recommendations = []

    for issue in issues:

        if "lento" in issue:
            recommendations.append("Otimizar fluxo e reduzir chamadas API")

        if "falhou" in issue:
            recommendations.append("Adicionar tratamento de erro")

    return list(set(recommendations))