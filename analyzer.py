def analyze_file(filename):

    findings = []

    with open(filename, "r") as file:
        code = file.read()

    if "password =" in code:
        findings.append({
            "title":"Hardcoded Password",
            "severity":"High",
            "description":"Password is directly stored in source code.",
            "recommendation":"Store passwords securely."
        })

    if "eval(" in code:
        findings.append({
            "title":"Use of eval()",
            "severity":"Critical",
            "description":"eval() can execute malicious code.",
            "recommendation":"Use ast.literal_eval()."
        })

    if "except:" in code:
        findings.append({
            "title":"Weak Exception Handling",
            "severity":"Medium",
            "description":"Generic exception handling hides errors.",
            "recommendation":"Catch specific exceptions."
        })

    return findings