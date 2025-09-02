from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="Financebot Chatbot")

app.include_router(router)

@app.get("/")
def root():
    var = True
    return {"status": "Chatbot Service is running"}
