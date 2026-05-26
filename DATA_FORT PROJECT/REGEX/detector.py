import re
from REGEX.patterns import (
    AADHAAR_REGEX,
    CREDIT_CARD_REGEX,
    API_KEY_REGEX,
    JWT_REGEX,
    PHONE_REGEX,
    PAN_REGEX,
    EMAIL_REGEX
)

def detect_sensitive_data(file_path):
    patterns = {
        "Email": EMAIL_REGEX,
        "Phone": PHONE_REGEX,
        "PAN": PAN_REGEX,
        "Aadhaar": AADHAAR_REGEX,
        "Credit Card": CREDIT_CARD_REGEX,
        "API Key": API_KEY_REGEX,
        "JWT": JWT_REGEX
    }

    findings = []
    try:
        with open(file_path, "r", errors="ignore") as file:
            content = file.read()
            for label, regex in patterns.items():
                matches = re.findall(regex, content)
                if matches:
                    findings.append((label, matches))
    except Exception as e:
        print(f"Error processing file: {e}")

    return findings   # always return, even if empty
