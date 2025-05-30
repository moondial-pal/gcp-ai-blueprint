from fastapi import FastAPI, Request
from google.cloud import aiplatform
from decouple import config

app = FastAPI()

PROJECT_ID = config("PROJECT_ID")
VERTEX_REGION = config("VERTEX_REGION")

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    user_input = data.get("message", "")
    agent = route_to_agent(user_input)
    response = call_vertex_ai(user_input, agent)
    return {"response": response}

def route_to_agent(message: str) -> str:
    if "outlook" in message.lower():
        return "it"
    elif "vacation" in message.lower():
        return "hr"
    return "general"

def call_vertex_ai(message: str, agent: str) -> str:
    aiplatform.init(project=PROJECT_ID, location=VERTEX_REGION)
    model = aiplatform.LanguageModel.from_pretrained("text-bison")
    prediction = model.predict(message)
    return prediction.text
