def ends_with_digit(text):
    # Remove trailing and leading whitespace from the string
    text = text.strip()
    # Checks whether the string is non-empty and ends with a digit
    if text and text[-1] in "0123456789":
        return True
    # Returns False if the string is empty or does not end with a digit
    return False
