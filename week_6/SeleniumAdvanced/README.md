# Selenium Advanced

This module contains advanced Selenium automation examples including explicit waits, screenshot capturing, file uploads, and Page Object Model (POM) patterns.

## Directory Structure
- `test_waits.py` - Synchronization using `WebDriverWait` and `expected_conditions`.
- `test_screenshot.py` - Saving visual screenshots of web application states.
- `test_file_upload.py` - Automating file selection and submission elements.
- `pom/` - Page Object Model encapsulating web element locators and page actions:
  - `dashboard_page.py` - Page Object for dashboard interactions.
  - `profile_page.py` - Page Object for user profile interactions.

## How to Run
```bash
pytest SeleniumAdvanced/
```
