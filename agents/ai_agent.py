from agents.phi_agent import ask_phi

def analyze_with_ai(data):

    try:

        prompt = f"""
Você é um micro-agente especialista em AIOps para Microsoft Power Platform.
Seu objetivo é analisar logs, telemetria, XMLs de erro, Solution Checker e eventos do Power Apps, Power Automate e Dataverse.
Você atua como um Agente Inteligente de Governança Low-Code.

Analise cuidadosamente os dados abaixo:


{data}

Identifique: 

1. Resumo técnico do problema
2. Possível causa raiz
3. Impacto no ambiente
4. Nível de criticidade
5. Recomendações técnicas
6. Possível solução
7. Melhorias preventivas

Responda de forma detalhada e profissional.

.
"""

        result = ask_phi(prompt)

        return result

    except Exception as e:
        return f"Erro: {str(e)}"