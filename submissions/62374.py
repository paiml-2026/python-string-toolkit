
def count_vowel_groups(text):
    # Store all vowels in lowercase and uppercase
    vowels = "aeiouAEIOU"

    # Initialize the number of vowel groups
    count = 0

    # Track whether the previous character was a vowel
    in_group = False

    # Check each character in the text
    for ch in text:
        if ch in vowels:
            # Count only when a new vowel group begins
            if not in_group:
                count += 1

            # Mark that we are inside a vowel group
            in_group = True
        else:
            # A consonant or other character ends the group
            in_group = False

    # Return the total number of vowel groups
    return count


# Test example
word = "beautiful"
result = count_vowel_groups(word)

# Display the input and expected result
print("Input:", word)
print("Expected output: 3")
print("Actual output:", result)

# Verify the function using an assertion
assert result == 3, "Test failed!"
print("Test passed!")
