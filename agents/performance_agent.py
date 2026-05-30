def analyze_performance(df):

    issues = []

    # junta todas as colunas em texto
    full_text = df.fillna("").astype(str).apply(
    lambda row: " ".join(row.values),
    axis=1
    )

    # palavras críticas
    critical_keywords = [
        "error",
        "exception",
        "failed",
        "failure",
        "critical",
        "timeout",
        "unauthorized",
        "forbidden",
        "invalid",
        "crash"
    ]

    for line in full_text:

        lower_line = line.lower()

        for keyword in critical_keywords:

            if keyword in lower_line:

                issues.append(
                    f"Possível problema encontrado: {line[:200]}"
                )

                break

    # caso nenhum problema seja encontrado
    if not issues:

        issues.append("Nenhum problema crítico encontrado")

    return issues