from fastapi.testclient import TestClient
from app.main import app  

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_ask_question_valid():
    payload = {"question": "How do I reset my account password?"}
    response = client.post("/ask", json=payload)
    
    assert response.status_code == 200
    assert response.json()["status"] == "success"
    assert response.json()["question"] == "How do I reset my account password?"

def test_ask_short_question():
    payload = {"question": "Why?"} 
    response = client.post("/ask", json=payload)
    
    assert response.status_code == 422
    assert "detail" in response.json()

def test_ask_question_missing_field():
    payload = {}
    response = client.post("/ask", json=payload)
    
    assert response.status_code == 422
