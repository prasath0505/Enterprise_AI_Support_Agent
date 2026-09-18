from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
async def get_health():
    return {"status": "healthy"}

@app.post("/ask")
async def ask_question(question: str):
    # Placeholder for processing the question and generating a response
    response = f"You asked: {question}. This is a placeholder response."
    return {"response": response}
