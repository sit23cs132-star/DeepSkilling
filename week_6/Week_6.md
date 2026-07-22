# Week 6 – Selenium Advanced & DevOps Basics

## Contents
- **SeleniumAdvanced/** → Advanced Selenium scripts (waits, screenshots, file upload, POM)
- **DevOpsBasics/** → Docker setup, CI/CD pipelines (GitHub Actions, Jenkins)

## How to Run
1. Install dependencies: `pip install selenium flask pytest`
2. Run Selenium tests: `pytest SeleniumAdvanced/`
3. Build Docker image: `docker build -t week6-app .`
4. Run container: `docker run -p 5000:5000 week6-app`
5. CI/CD → GitHub Actions auto-runs on push, Jenkins pipeline for deployment.
