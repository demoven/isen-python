# ISEN Python Project 🐍

**Educational Project | CI/CD & Testing Implementation**

This repository contains a Django web application provided by a professor as a base for an advanced software engineering exercise.

**My Contribution:**
While the core application logic was provided, my role in this project was to design and implement the entire **Quality Assurance and DevOps ecosystem**. I was responsible for setting up the **CI/CD pipelines** using GitHub Actions and writing the comprehensive **Test Suites** (Unit, Integration, and E2E) to ensure the robustness of the application.

## 🎯 Educational Goal

The main objective of this repository is to demonstrate a complete software automation chain on an existing codebase. The business logic serves as a context to experiment with:

* **GitHub Actions**: Configuration of complex workflows from scratch.
* **Unit & Integration Tests**: Writing tests for the Python/Django backend using `pytest`.
* **E2E (End-to-End) Tests**: Implementing user interface scenarios with **Cypress**.
* **Code Quality (Linting)**: Automating style checks and static analysis.
* **Security (SAST)**: Integrating security scanning tools.
* **Containerization**: Dockerizing the application for deployment.

## ⚙️ CI/CD Pipelines (My Implementation)

I integrated several GitHub Actions workflows located in `.github/workflows/`:

| Workflow | Description |
| :--- | :--- |
| **Lint** (`lint.yml`) | Checks code quality (PEP8, syntax errors). |
| **Tests Backend** (`tests.yml`) | Runs unit and integration tests using `pytest`. |
| **Tests E2E** (`cypress.yml`) | Runs user interface tests with Cypress. |
| **Security** (`sast.yml`) | Analyzes code to detect security vulnerabilities (SAST). |
| **Container** (`container.yml`) | Builds the application's Docker image. |

## 🧪 Testing Strategy

I implemented a complete testing pyramid to cover the provided code:

1.  **Unit Tests** (`unit_tests/`): Test models, URLs, and forms in isolation.
2.  **Integration Tests** (`integration_tests/`): Verify interactions between components (e.g., authentication flow, adding favorites).
3.  **End-to-End Tests** (`cypress/e2e/`): Simulate a real user's journey in the browser (Login, Navigation, Filters).

## ✨ App Features (Base Project)

The provided Django application includes the following features:

* **Authentication**: Registration, Login, Profile management.
* **Catalog**: Display a list of products.
* **Favorites**: Ability for a logged-in user to add products to their favorites.
* **Back-office**: Django administration interface to manage users and products.

## 🛠️ Tech Stack

* **Backend**: Python 3, Django
* **Frontend**: HTML5, CSS3, JavaScript
* **Database**: SQLite (default)
* **Tests**: Pytest, Cypress
* **CI/CD**: GitHub Actions, Docker
**Backend Tests (Pytest):**
```bash
pytest
