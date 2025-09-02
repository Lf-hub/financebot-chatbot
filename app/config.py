import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    AI_URL: str = os.getenv("AI_URL", "http://localhost:8001/parse")
    BACKEND_URL: str = os.getenv("BACKEND_URL", "http://localhost:8002/transaction")

settings = Settings()