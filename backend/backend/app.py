
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="Chatmini API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def home():
    return {
        "name": "Chatmini",
        "status": "online",
        "message": "Welcome to Chatmini!"
    }

@app.post("/chat")
def chat(request: ChatRequest):
    message = request.message.strip()

    if not message:
        return {"reply": "Please type a message."}

    return {
        "reply": (
            "Hi! I'm Chatmini, your AI assistant. "
            "I'm still learning, but I'm happy to chat with you. "
            "You said: " + message
        )
    }
