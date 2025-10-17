from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import Optional
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Define the data schema for /eval POST requests
class EvalNotification(BaseModel):
    email: str
    task: str
    round: int
    nonce: str
    repo_url: str
    commit_sha: str
    pages_url: str
    

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["*"],
    expose_headers=["*"]
)

@app.post("/eval")
async def receive_evaluation(data: EvalNotification):
    print("✅ Evaluation data received:")
    print(f"  📧 Email: {data.email}")
    print(f"  📝 Task: {data.task}")
    print(f"  🔁 Round: {data.round}")
    print(f"  🔐 Nonce: {data.nonce}")
    print(f"  🔗 Repo: {data.repo_url}")
    print(f"  🔖 Commit: {data.commit_sha}")
    print(f"  🌍 Pages URL: {data.pages_url}")

    # Optionally: store or log this into a DB or file
    # You can also trigger post-evaluation actions here

    return {"status": "ok", "message": "Evaluation received"}


