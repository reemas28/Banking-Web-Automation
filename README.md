# Banking Web Application Testing


**Project:** Banking Web Application Testing (Demo) — Automated with Selenium (Python) using POM.


## Overview
This project demonstrates manual and automated testing for a demo banking web application. It includes:
- Manual test cases for login and fund transfer.
- Automated tests using Selenium WebDriver with Page Object Model.
- Reusable driver helper using webdriver-manager.


## Tech stack
- Python
- Selenium WebDriver
- pytest
- webdriver-manager


## Project structure
See the project tree in the repo root. Tests are under `tests/`, page objects under `pages/`.


## How to run
# 1. Create a virtual environment and install requirements:


python -m venv venv
source venv/bin/activate # or venv\Scripts\activate on Windows
pip install -r requirements.txt


# 2. Run Tests

pytest -q
# For headless mode
pytest -q --headless