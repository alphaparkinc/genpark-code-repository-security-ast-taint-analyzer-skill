from client import CodeRepositorySecurityAstTaintAnalyzerClient

def main():
    client = CodeRepositorySecurityAstTaintAnalyzerClient()
    res = client.analyze_repository("src/", "OWASP_TOP_10")
    print(f"Overall Risk Score: {res['overall_risk_score']}")
    for v in res["vulnerabilities_found"]:
        print(f"  [{v['severity']}] {v['type']} in {v['file']}:L{v['line']}")

if __name__ == "__main__":
    main()
