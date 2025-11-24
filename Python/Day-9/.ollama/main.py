from fastapi import FastAPI
from models import  SOAPRequest
from models import Query
from models import ConversationRequest
import requests
import json

app = FastAPI()


OLLAMA_URL = "http://localhost:11434/api/generate"

@app.post("/soap")
async def generate_soap_notes(req:SOAPRequest):
    prompt = f"""
Generate SOAP medical notes based on the patient conversation below.

Patient Text:
{req.patient_text}

Return the output STRICTLY in JSON with this structure:

{{
"Subjective": "",
"Objective": "",
"Assessment": "",
"Plan": ""
}}
"""

    payload = {
        "model": "qwen3:0.6b",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)
    data = response.json()

    return {"soap_notes": data.get("response")}

@app.post("/progress-notes")
def generate_progress_notes(req: ConversationRequest):
    conversation_text = "\n".join(req.messages)

    prompt = f"""
    You are a medical assistant. Generate Progress Notes based on this conversation:

    {conversation_text}

    Return output ONLY in JSON:

    {{
    "ConversationSummary": "",
    "PatientStatements": "",
    "ClinicianStatements": "",
    "Assessment": "",
    "TreatmentGiven": "",
    "PatientResponse": "",
    "NextSteps": ""
    }}
    """

    payload = {
        "model": "qwen3:0.6b",
        "prompt": prompt,
        "stream": False
    }

    r = requests.post(OLLAMA_URL, json=payload)
    text = r.json().get("response", "")

    return {"progress_notes": json.loads(text)}

@app.post("/ask")
async def ask(query: Query):
    payload = {
        "model": "qwen3:0.6b", 
        "prompt": query.prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)
    data = response.json()

    soap = json.loads(data.get("response"))

    return soap
