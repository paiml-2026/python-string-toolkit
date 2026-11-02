def count_uppercase(text):
    """Return the number of uppercase letters in text."""
    count = 0

    for ch in text:
        if ch.isupper():
            count += 1

    return count
