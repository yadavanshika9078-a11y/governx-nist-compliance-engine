import json


class SecurityScanner:
    """
    Reads cloud configuration
    Detects security issues
    Returns findings
    """

    def __init__(self, file_path):
        self.file_path = file_path

    def load_configuration(self):
        with open(self.file_path, "r") as file:
            return json.load(file)

    def load_nist_mapping(self):
        with open("backend/data/nist_mapping.json", "r") as file:
           return json.load(file)
    
    def scan(self):
        config = self.load_configuration()
        nist_mapping = self.load_nist_mapping()

        findings = []

        # Storage Check
        if config["storage"]["public_bucket"]:
            findings.append({
                "id": "ST001",
                "category": "Storage",
                "issue": "Public Storage Bucket",
                "severity": "High"
            })

        if not config["storage"]["encryption_enabled"]:
            findings.append({
                "id": "ST002",
                "category": "Storage",
                "issue": "Encryption Disabled",
                "severity": "Medium"
            })

        # IAM Check
        if not config["iam"]["mfa_enabled"]:
            findings.append({
                "id": "IAM001",
                "category": "IAM",
                "issue": "MFA Disabled",
                "severity": "High"
            })

        if config["iam"]["inactive_users"] > 0:
            findings.append({
                "id": "IAM002",
                "category": "IAM",
                "issue": f'{config["iam"]["inactive_users"]} Inactive Users',
                "severity": "Low"
            })

        if config["iam"]["weak_password_policy"]:
            findings.append({
                "id": "IAM003",
                "category": "IAM",
                "issue": "Weak Password Policy",
                "severity": "Medium"
            })

        # Network Check
        if config["network"]["open_security_group"]:
            findings.append({
                "id": "NET001",
                "category": "Network",
                "issue": "Open Security Group",
                "severity": "Critical"
            })

        # Logging Check
        if not config["logging"]["cloudtrail_enabled"]:
            findings.append({
                "id": "LOG001",
                "category": "Logging",
                "issue": "CloudTrail Disabled",
                "severity": "Medium"
            })

        for finding in findings:
            
            finding_id = finding["id"]

            if finding_id in nist_mapping:

               finding["nist_category"] = nist_mapping[finding_id]["nist_category"]

               finding["nist_title"] = nist_mapping[finding_id]["title"]
        return findings