def analyze_performance(df):

    issues = []

    for _, row in df.iterrows():

        if row["duration"] > 5000:
            issues.append(f"{row['operation']} está lento")

        if row["success"] == False:
            issues.append(f"{row['operation']} falhou")

    return issues