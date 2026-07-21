# GovernX: Automated NIST CSF 2.0 Compliance Engine

GovernX is a cybersecurity dashboard that assesses cloud-security configurations, maps findings to NIST CSF 2.0 categories, calculates a simple risk score, and presents prioritized remediation actions.

## Problem

Security compliance is often tracked manually in spreadsheets. This makes it difficult to identify configuration gaps, connect technical issues to business risk, and report progress clearly.

## Project Goal

Build a safe demonstration platform that:

- Reads mock cloud-security configuration data
- Detects common security misconfigurations
- Maps findings to NIST CSF 2.0 functions
- Calculates an overall compliance score
- Displays risks and recommended actions in a dashboard

## Initial Security Checks

1. Public storage bucket detected
2. Storage encryption disabled
3. Open security-group port detected
4. MFA disabled for a user
5. Inactive user account detected
6. Weak IAM policy detected
7. Logging disabled
8. Backup configuration missing


## Technology Stack

- Backend: Python and FastAPI
- Database: SQLite initially, PostgreSQL later
- Frontend: React
- Testing: Pytest
- Data: Mock AWS-style JSON data

## Project Status

- Internship project started: 17 July 2026
- Repository and initial project documentation created: 19 July 2026
- Current focus: Catching up on project setup and mock cloud-security data

✔ Repository Setup Completed

✔ Backend Structure Completed

✔ Mock Cloud Configuration Added

✔ Security Scanner Completed

✔ Scan API Working

Next:
NIST CSF Mapping

## Safety Note

This project uses mock/sample cloud data only. It will not access real cloud accounts or store credentials.