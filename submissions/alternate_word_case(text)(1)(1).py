def alternate_word_case(text):
    """Alternate uppercase and lowercase letters within each word, starting uppercase."""
    # Store the converted characters so they can be joined at the end.
    result = []

    # The first alphabetic character of each word should be uppercase.
    uppercase = True

    # Process the input one character at a time.
    for char in text:
        if char.isalpha():
            # Convert the letter according to the current case flag.
            result.append(char.upper() if uppercase else char.lower())

            # Switch the case for the next alphabetic character.
            uppercase = not uppercase
        else:
            # Keep non-letter characters (such as punctuation and digits) unchanged.
            result.append(char)

            # Reset the pattern after whitespace so the next word starts uppercase.
            if char.isspace():
                uppercase = True

    # Combine the converted characters into one string and return it.
    return ''.join(result)
