import requests
import pandas as pd

API_URL = "http://localhost:11434/api/generate"

def analyze_with_ai(file_path):

    try:
        df = pd.read_csv(file_path)

        # 🔹 limitar tamanho (importante!)
        sample = df.head(20).to_string()

        prompt = f"""
        Você é um especialista em análise de logs.

        Analise os dados abaixo:

        {sample}

        Identifique:
        - Problemas
        - Possíveis erros
        - Sugestões de melhoria

        Seja direto.
        """

        response = requests.post(
            API_URL,
            json={
                "model": "phi3",
                "prompt": prompt,
                "stream": False
            },
            timeout=30
        )

        result = response.json()

        return result.get("response", "Erro ao analisar")

    except Exception as e:
        return f"Erro: {str(e)}"