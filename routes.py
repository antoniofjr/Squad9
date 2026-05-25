from fastapi import APIRouter
from utils.file_reader import read_file
from fastapi import Body

from agents.performance_agent import analyze_performance
from agents.risk_agent import calculate_risk
from agents.recommendation_agent import generate_recommendations
from agents.ai_agent import analyze_with_ai

from agents.phi_agent import ask_phi

router = APIRouter()

@router.get("/analyze")
def analyze(file_path: str):

    df = read_file(file_path)

    if df is None:
        return {"error": "Erro ao ler arquivo"}

    issues = analyze_performance(df)

    risk = calculate_risk(issues)

    recommendations = generate_recommendations(issues)

    ai_result = analyze_with_ai(issues)

    return {
        "issues": issues,
        "risk": risk,
        "recommendations": recommendations,
        "ai_analysis": ai_result
    }


@router.get("/ask-ai")
def ask_ai(question: str):

    response = ask_phi(question)

    return {
        "response": response
    }

@router.post("/analyze-custom")
def analyze_custom(payload: dict = Body(...)):

    text = payload.get("text", "")
    file_path = payload.get("file_path", "")

    df = read_file(file_path)

    if df is None:
        return {
            "error": "Erro ao ler arquivo"
        }

    sample = df.astype(str).head(20).to_string()

    prompt = f"""
    Você é um especialista em análise de logs Power Platform.

    O usuário quer analisar o seguinte:

    {text}

    Dados do arquivo:

    {sample}

    Identifique:
    - problemas
    - erros
    - riscos
    - falhas
    - possíveis soluções

    Responda de forma técnica e detalhada.
    """

    response = ask_phi(prompt)

    return {
        "analysis": response
    }