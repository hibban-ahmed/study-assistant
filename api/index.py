from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
from dotenv import load_dotenv
import requests

load_dotenv()

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class RequestPayload(BaseModel):
    content: str
    prompt: str
    model: str

@app.post("/generate")
async def generate_response(data: RequestPayload):
    input_text = f"Resources:\n{data.content}\n\nPrompt:\n{data.prompt}"

    if data.model == "gemini":
        api_key = os.getenv("GEMINI_API_KEY")
        # Replace with actual Gemini endpoint
        response = requests.post(
            "https://api.gemini.fake/generate",  # update this!
            headers={"Authorization": f"Bearer {api_key}"},
            json={"input": input_text}
        )
    elif data.model == "llama":
        api_key = os.getenv("LLAMA_API_KEY")
        # Replace with actual LLaMA endpoint
        response = requests.post(
            "https://api.llama.fake/generate",  # update this!
            headers={"Authorization": f"Bearer {api_key}"},
            json={"prompt": input_text}
        )
    else:
        return {"error": "Invalid model selected"}

    return {"output": response.json()}
