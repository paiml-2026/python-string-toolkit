def normalize_whitespace(text):
    # Split the text using whitespace (spaces, tabs, newlines)
    words = text.split()

    # Join the words with a single space between them
    normalized_text = " ".join(words)

    # Return the normalized text
    return normalized_text
