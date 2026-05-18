from fastapi import APIRouter
from utils.file_reader import read_csv

from agents.performance_agent import analyze_performance
from agents.risk_agent import calculate_risk
from agents.recommendation_agent import generate_recommendations
from agents.ai_agent import analyze_with_ai

from agents.phi_agent import ask_phi

router = APIRouter()

@router.get("/analyze")
def analyze(file_path: str):

    df = read_csv(file_path)

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