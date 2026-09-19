from fastapi import FastAPI
from pydantic import BaseModel, Field

app=FastAPI()

class QuestionModel(BaseModel):
    question: str = Field(
        ..., 
        min_length=5, 
        max_length=500, 
        description="The query string sent to the AI support agent."
    )
    


@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.post("/ask")
async def ask_question(Question: QuestionModel):
    
    return {"response": "This is a placeholder response.", "question": Question.question, "status": "success"}