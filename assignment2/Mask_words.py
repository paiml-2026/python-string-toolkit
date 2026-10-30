import re

def mask_word(text, target):
    if not target:
        return text

    replacement = "*" * len(target)
    pattern = rf"\b{re.escape(target)}\b"

    return re.sub(pattern, replacement, text)
