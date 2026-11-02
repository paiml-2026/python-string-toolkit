
def find_character_position(text, ch):
    # Check each character in the string
    for i in range(len(text)):
        # If the character matches, return its index
        if text[i] == ch:
            return i

    # Return -1 if the character is not found
    return -1
