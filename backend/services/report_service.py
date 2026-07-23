class ReportGenerator:

    def generate(self, findings):

        report = []
        report.append("=" * 40)
        report.append("GovernX Security Report")
        report.append("=" * 40)
        report.append("")

        report.append(f"Total Findings : {len(findings)}")
        report.append("")

        for finding in findings:

            report.append("-" * 40)
            report.append(f"Severity : {finding['severity']}")
            report.append(f"ID       : {finding['id']}")
            report.append(f"Issue    : {finding['issue']}")
            report.append(f"Category : {finding['category']}")
            report.append(f"NIST     : {finding['nist_category']}")
            report.append(f"Title    : {finding['nist_title']}")
            report.append("")

        return "\n".join(report)