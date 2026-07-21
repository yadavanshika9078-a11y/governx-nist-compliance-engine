# GovernX Daily Work Log

## 19 July 2026 — Repository Setup and Planning

### Goal

Set up the project repository and define the GovernX MVP.

### Completed

- Created the GitHub repository
- Cloned the repository locally using GitHub Desktop
- Defined the project scope and eight initial security checks
- Created the development plan

### Learned

- A Git repository stores a project’s history.
- GitHub Desktop detects local changes and publishes commits to GitHub.

### Next Step

Create mock cloud-security data and start the Python backend structure.

### Catch-up Plan

- 20 July: Create mock cloud-security data
- 21 July: Build the first Python security scanner
- 22 July: Map findings to NIST CSF 2.0 categories
- 23 July: Add scoring and basic test cases

## 20 July 2026 — Backend Initialization

### Goal

Initialize the Python backend and create the foundation for the GovernX compliance engine.

### Completed

- Created the backend project structure.
- Added Python package initialization files (__init__.py).
- Created Python virtual environment (venv).
- Installed project dependencies:
  - Flask
  - Flask-CORS
  - python-dotenv
- Generated requirements.txt.
- Created config.py for application configuration.
- Added support for environment variables using .env.
- Created the Flask application (app.py).
- Implemented the first REST API endpoint.
- Successfully started the Flask development server.
- Verified the backend by accessing http://127.0.0.1:5000/.

### Learned

- How Python virtual environments isolate project dependencies.
- Why requirements.txt is important for reproducible development.
- The purpose of __init__.py files in Python packages.
- How Flask routes work.
- How configuration files improve project maintainability.
- How environment variables help keep sensitive settings separate from code.

### API Tested

**GET /**

Response

```json
{
    "message": "Welcome to GovernX",
    "status": "Backend is running successfully",
    "version": "1.0.0"
}
```

### Problems Faced

- Understanding Python package structure.
- Setting up the virtual environment correctly.
- Learning how Flask applications are organized.

### Status

✅ Backend foundation completed successfully.

### Next Step

Build the API architecture and implement the first cloud security scanner module.

## 21 July 2026 — Day 3

### Goal

Build the first mock cloud security scanner.

### Completed

- Created mock cloud configuration JSON
- Implemented SecurityScanner class
- Added security rule checks
- Added /scan API endpoint
- Successfully returned security findings in JSON format
- Tested backend using Flask

### Learned

- Reading JSON files in Python
- Creating classes and methods
- Returning JSON responses with Flask
- Basic cloud security scanning workflow

### Next Step

Map scanner findings to NIST CSF 2.0 categories and improve report format.