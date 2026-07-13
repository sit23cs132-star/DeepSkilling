# Week 2 – Backend Development & Advanced Testing

This directory contains backend application implementations across multiple Python frameworks along with advanced testing suites for Week 2 of the FSE Deep Skilling program.

## Directory Contents

### 1. Django Backend (`Django_Backend/`)
A fully-featured Django REST Framework project managing a course list database with two entities: `Course` and `Department`.
- `manage.py` → Django administrative script.
- `coursemanager/` → Main Django project configurations (`settings.py`, `urls.py`).
- `courses/` → Courses application (`models.py`, `views.py`, `serializers.py`, `urls.py`, `tests.py`).

### 2. Flask Backend (`Flask_Backend/`)
A course management service developed with Flask and SQLAlchemy.
- `app.py` → Application entry point.
- `config.py` → Database and application configuration.
- `courses/` → Flask routes and database models.

### 3. FastAPI Backend (`FastAPI_Backend/`)
A modern, fast FastAPI implementation for course management.
- `main.py` → API routing and endpoint logic.
- `models.py` → SQLAlchemy models.
- `schemas.py` → Pydantic models for validation.
- `tests.py` → Integration test suite using FastAPI's TestClient.

### 4. Advanced Unit Testing (`UnitTesting_Advanced/`)
Advanced test cases demonstrating `pytest` fixtures and database mocking.
- `conftest.py` → Pytest fixtures.
- `test_models.py` → Testing database model behaviour.
- `test_api_endpoints.py` → Testing REST API endpoints.

---

## How to Run

### Django Backend
```bash
cd Django_Backend
python manage.py migrate
python manage.py runserver
```

### Flask Backend
```bash
cd Flask_Backend
pip install Flask Flask-SQLAlchemy
python app.py
```

### FastAPI Backend
```bash
cd FastAPI_Backend
pip install fastapi uvicorn sqlalchemy
uvicorn main:app --reload
```
