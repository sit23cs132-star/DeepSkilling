import pytest
import requests

BASE_URL = "http://127.0.0.1:8000/api/courses/"

def test_get_courses():
    response = requests.get(BASE_URL)
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_course():
    payload = {"name": "Python Basics", "code": "PY101", "credits": 3}
    response = requests.post(BASE_URL, json=payload)
    assert response.status_code == 201
    assert response.json()["name"] == "Python Basics"
