# patterns.py
EMAIL_REGEX = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
PHONE_REGEX = r"\b\d{10}\b"
PAN_REGEX = r"[A-Z]{5}[0-9]{4}[A-Z]{1}"
AADHAAR_REGEX = r"\b\d{4}\s\d{4}\s\d{4}\b"
CREDIT_CARD_REGEX = r"\b(?:\d[ -]*?){13,16}\b"
API_KEY_REGEX = r"[A-Za-z0-9]{32,}"
JWT_REGEX = r"^[A-Za-z0-9-_]+\.[A-Za-z0-9-_]+\.[A-Za-z0-9-_]+$"