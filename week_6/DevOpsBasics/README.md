# DevOps Basics

This module contains Docker configuration, Compose service definitions, Flask web app source, and CI/CD pipelines (GitHub Actions & Jenkins).

## Directory Structure
- `Dockerfile` - Container specification for the Flask application.
- `docker-compose.yml` - Multi-container setup and port mapping.
- `app/` - Source code for Flask application and `requirements.txt`.
- `ci-cd/` - CI/CD pipeline definitions:
  - `github-actions.yml` - GitHub Actions CI workflow config.
  - `jenkinsfile` - Jenkins declarative pipeline script.

## How to Run
1. Build Docker image:
   ```bash
   docker build -t week6-app .
   ```
2. Run container:
   ```bash
   docker run -p 5000:5000 week6-app
   ```
3. Run with Docker Compose:
   ```bash
   docker-compose up --build
   ```
