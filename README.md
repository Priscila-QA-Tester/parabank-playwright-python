# Parabank E2E Automation - Python & Playwright

This repository contains an automated end-to-end (E2E) test suite for the Parabank web application, built using **Python**, **Playwright**, and **Pytest**. 

## 🚀 Project Overview

The goal of this project is to validate core banking operations, transaction flows, and user registration processes on the Parabank platform. It demonstrates the ability to create robust, maintainable, and scalable test automation architectures.

### Key Features
*   **End-to-End Testing:** Covers critical user journeys including registration, login, and error validation.
*   **Python & Playwright:** Utilizes modern automation tools for fast and reliable browser interaction.
*   **Pytest Framework:** Leverages Pytest for test structuring, execution, and reporting.
*   **Continuous Integration:** Integrated with **GitHub Actions** to automatically run the test suite on every code push, ensuring continuous quality and stable delivery.
*   **Business Rule Validation:** Includes rigorous checks for frontend boundaries, missing mandatory fields, and data duplication scenarios.

## 🛠️ Technology Stack
*   [Python 3](https://www.python.org/)
*   [Playwright for Python](https://playwright.dev/python/)
*   [Pytest](https://docs.pytest.org/)
*   [GitHub Actions](https://github.com/features/actions) (CI/CD)

## ⚙️ How to Run Locally

### Prerequisites
Make sure you have Python 3 installed on your machine.

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Priscila-QA-Tester/parabank-playwright-python.git
   ```
2. Navigate to the project directory:
   ```bash
   cd parabank-playwright-python
   ```
3. Create and activate a virtual environment:
   ```bash
   # On Windows (PowerShell):
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```
4. Install dependencies:
   ```bash
   pip install pytest playwright pytest-playwright
   playwright install
   ```

### Execution
Run the test suite using Pytest:
```bash
pytest test_cadastro.py
```
To run the tests in headed mode (visible browser):
```bash
pytest test_cadastro.py --headed
```

---
*This project was developed as a portfolio showcase for QA Automation.*
