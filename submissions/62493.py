def last_word(text):
    """Return the last word of a string."""

    # Remove leading/trailing whitespace and split the string into words
    words = text.strip().split()

    # If the string is empty or contains only spaces, there is no last word
    if not words:
        return ""

    # The last item in the list is the last word
    return words[-1]


