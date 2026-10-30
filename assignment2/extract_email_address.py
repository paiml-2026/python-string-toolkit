import re

def extract_email_addresses(text):
    pattern = r'[\w.-]+@[\w.-]+\.\w+'
    return re.findall(pattern, text)
