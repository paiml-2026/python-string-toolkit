def replace_word(text, old, new):
    """
    Replace whole-word matches of old with new.
    """
    words = text.split()
    result = []

    for word in words:
        if word == old:
            result.append(new)
        else:
            result.append(word)

    return " ".join(result)


# Test Case 1
# Input: ("cat and cat", "cat", "dog")
# Expected Output: "dog and dog"

# Test Case 2
# Input: ("hello world", "hello", "hi")
# Expected Output: "hi world"

# Test Case 3
# Input: ("apple banana apple", "apple", "mango")
# Expected Output: "mango banana mango"

# Test Case 4
# Input: ("cat category", "cat", "dog")
# Expected Output: "dog category"

# Test Case 5
# Input: ("hello there", "bye", "goodbye")
# Expected Output: "hello there"
