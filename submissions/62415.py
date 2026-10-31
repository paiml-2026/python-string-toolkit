def keep_letters(text):
    # Create an empty string to store letters
    result = ""

    # Check each character in the input text
    for char in text:
        # Keep the character only if it is a letter
        if char.isalpha():
            result += char

    # Return the string containing only letters
    return result

print(keep_letters("a1b2!"))      # ab
