
def alternate_case(text):
    """
    Convert letters to alternating uppercase and lowercase,
    starting with uppercase.

    Non-letter characters (spaces, digits, punctuation)
    are preserved and do not affect the letter sequence.

    Example:
        alternate_case("python") -> "PyThOn"
    """
    result = ""  # Stores the final string
    letter_position = 0  # Counts only letters, starting at 0

    # Process each character in the input string
    for ch in text:
        if ch.isalpha():  # Check whether the character is a letter

            # Uppercase letters at even positions: 0, 2, 4...
            if letter_position % 2 == 0:
                result += ch.upper()

            # Lowercase letters at odd positions: 1, 3, 5...
            else:
                result += ch.lower()

            # Increase the position only for letters
            letter_position += 1

        else:
            # Keep spaces, digits, and punctuation unchanged
            result += ch

    # Return the completed string
    return result


# -------------------- TEST CASES --------------------

# Test 1: Normal lowercase string
print(alternate_case("python"))       # Expected: PyThOn

# Test 2: String containing uppercase and lowercase letters
print(alternate_case("HeLLo"))        # Expected: HeLlO

# Test 3: String containing spaces
print(alternate_case("hello world"))  # Expected: HeLlO WoRlD

# Test 4: String containing digits and punctuation
print(alternate_case("abc123!"))      # Expected: AbC123!

# Test 5: Empty string
print(alternate_case(""))             # Expected: ""

# Test 6: Single letter
print(alternate_case("a"))            # Expected: A

# Test 7: All uppercase letters
print(alternate_case("PYTHON"))       # Expected: PyThOn
