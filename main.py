from fastapi import FastAPI
from routes import router

app = FastAPI(title="AIOps Power Platform")

app.include_router(router)

@app.get("/")
def home():
    return {"message": "AIOps API rodando"}