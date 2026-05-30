from agents.phi_agent import ask_phi
from datetime import datetime
import os


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
"""

        
        result = ask_phi(prompt)

        
        os.makedirs("reports", exist_ok=True)

       
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        file_name = f"reports/relatorio_{timestamp}.txt"

        
        with open(file_name, "w", encoding="utf-8") as f:

            f.write("========== RELATÓRIO AIOPS ==========\n\n")

            f.write("===== DADOS ANALISADOS =====\n")
            f.write(str(data))
            f.write("\n\n")

            f.write("===== RESPOSTA DA IA =====\n")
            f.write(str(result))

        print(f"\nRelatório salvo em: {file_name}")

        return result

    except Exception as e:
        return f"Erro: {str(e)}"