def extract_acronyms(text):
    """
    Extracts acronyms from the given text.

    Args:
        text (str): The input text from which to extract acronyms.

    Returns:
        list: A list of unique acronyms found in the text.
    """
    import re

    # Regular expression pattern to match acronyms (e.g., NASA, FBI, U.S.A., etc.)
    
    pattern = r"\b(?:[A-Z]\.){2,}|\b[A-Z]{2,}\b"
    
    # Find all matches in the text
    acronyms = re.findall(pattern, text)
    
    # Return unique acronyms
    return list(set(acronyms))  