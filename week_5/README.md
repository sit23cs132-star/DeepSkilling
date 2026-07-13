# Week 5 – QA Concepts & Selenium Basics

This directory contains resources covering Software Quality Assurance (QA) fundamentals and browser automation using Selenium WebDriver in Python.

## Directory Contents

### 1. QA Concepts (`QA_Concepts/`)
- `qa_notes.md` → Overview of the defect lifecycle, test strategies, and automation criteria.
- `test_case_example.md` → A sample test case template detailing steps, expectations, and status reporting.

### 2. Selenium Automation (`SeleniumBasics/`)
- `test_login.py` → Basic Selenium script testing form input and submission validation.
- `test_navigation.py` → Selenium navigation flow validation testing.
- `conftest.py` → PyTest fixtures for managing the Selenium WebDriver lifecycle.
- `pom/` → Page Object Model (POM) design pattern structures:
  - `login_page.py` → Encapsulated locators and methods for the Login Page.
  - `home_page.py` → Encapsulated home page elements.

---

## How to Run
1. Install dependencies:
   ```bash
   pip install selenium pytest
   ```
2. Place ChromeDriver in your PATH.
3. Run tests using PyTest:
   ```bash
   pytest SeleniumBasics/
   ```
