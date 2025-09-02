from fastapi import FastAPI
from .routes import router

app = FastAPI(title="Financebot Chatbot")

app.include_router(router)

@app.get("/")
def root():
    return {"status": "Chatbot Service is running 🚀"}
