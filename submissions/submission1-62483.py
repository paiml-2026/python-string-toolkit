def first_word(text):
    # Split text into words
    words = text.split()

    # If text is empty or just spaces, return empty string
    if not words:
        return ""

    # Return the first word
    return words[0]
