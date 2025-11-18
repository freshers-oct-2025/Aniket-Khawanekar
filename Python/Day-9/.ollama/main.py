from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

class Query(BaseModel):
    prompt: str

OLLAMA_URL = "http://localhost:11434/api/generate"

@app.post("/ask")
async def ask(query: Query):
    payload = {
        "model": "qwen3:0.6b", 
        "prompt": query.prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)
    data = response.json()

    return {"answer": data.get("response")}
