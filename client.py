class CodeRepositorySecurityAstTaintAnalyzerClient:
    def analyze_repository(self, repository_path: str, ruleset: str = "OWASP_TOP_10") -> dict:
        vulns = [
            {"type": "SQL_INJECTION_RISK", "file": "db.py", "line": 42, "severity": "HIGH"},
            {"type": "UNSAFE_DESERIALIZATION", "file": "utils.py", "line": 108, "severity": "MEDIUM"}
        ]
        return {
            "vulnerabilities_found": vulns,
            "overall_risk_score": "MEDIUM_RISK"
        }
