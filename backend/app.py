from flask import Flask
from flask_cors import CORS

from config import Config
from services.scanner_service import SecurityScanner

app = Flask(__name__)
app.config.from_object(Config)

CORS(app)


@app.route("/")
def home():
    return {
        "message": "Welcome to GovernX",
        "version": Config.VERSION,
        "status": "Backend is running successfully"
    }

@app.route("/scan")
def scan():

    scanner = SecurityScanner("backend/data/cloud_config.json")

    findings = scanner.scan()

    return {
        "status": "Scan Completed",
        "total_findings": len(findings),
        "findings": findings
    }

if __name__ == "__main__":
    app.run(debug=Config.DEBUG)