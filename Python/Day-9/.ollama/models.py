from pydantic import BaseModel

class Query(BaseModel):
    prompt: str
    
class ConversationRequest(BaseModel):
    messages: list[str]

class SOAPRequest(BaseModel):
    patient_text:str