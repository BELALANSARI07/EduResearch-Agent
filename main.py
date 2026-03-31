from fastapi import FastAPI
from pydantic import BaseModel
from agent import EduAgent

# Initialize FastAPI app
app = FastAPI()

# Initialize your agent
agent = EduAgent()


# Request body schema
class QueryRequest(BaseModel):
    question: str


# Root endpoint (for testing)
@app.get("/")
def read_root():
    return {"message": "EduResearch Agent is running 🚀"}


# Main AI endpoint (IMPORTANT)
@app.post("/ask")
def ask_agent(request: QueryRequest):
    response = agent.run(request.question)
    return {"answer": response}