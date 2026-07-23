from flask import Flask, Response
from flask_cors import CORS

from config import Config

from services.scanner_service import SecurityScanner
from services.report_service import ReportGenerator

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

    generator = ReportGenerator()
    report = generator.generate(findings)

    return {
        "status": "Scan Completed",
        "total_findings": len(findings),
        "findings": findings,
        "report": report
    }

@app.route("/report")
def report():

    scanner = SecurityScanner("backend/data/cloud_config.json")

    findings = scanner.scan()

    generator = ReportGenerator()

    report = generator.generate(findings)

    return Response(report, mimetype="text/plain")

@app.route("/download-report")
def download_report():

    scanner = SecurityScanner("backend/data/cloud_config.json")
    findings = scanner.scan()

    generator = ReportGenerator()
    report = generator.generate(findings)

    return Response(
        report,
        mimetype="text/plain",
        headers={
            "Content-Disposition":
            "attachment; filename=governx_report.txt"
        }
    )

if __name__ == "__main__":
    app.run(debug=Config.DEBUG)