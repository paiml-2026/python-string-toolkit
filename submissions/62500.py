def shortest_word(text):
    """Return the first shortest whitespace-separated word in text."""
    words = text.split()
    if not words:
        return ""
    return min(words, key=len)
