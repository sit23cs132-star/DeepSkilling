from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_courses():
    response = client.get("/api/courses/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_course():
    payload = {"name": "Python", "code": "PY101", "credits": 3}
    response = client.post("/api/courses/", json=payload)
    assert response.status_code == 200
    assert response.json()["name"] == "Python"
