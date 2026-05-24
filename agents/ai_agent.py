from agents.phi_agent import ask_phi

def analyze_with_ai(data):

    try:

        prompt = f"""
Você é um especialista em análise de logs.

Analise os dados abaixo:

{data}

Identifique:
- Problemas
- Possíveis erros
- Sugestões de melhoria

Seja direto.
"""

        result = ask_phi(prompt)

        return result

    except Exception as e:
        return f"Erro: {str(e)}"