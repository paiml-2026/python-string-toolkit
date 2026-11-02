# Function to count unique characters in a string
def count_unique_characters(text):
    # Convert the string into a set to remove duplicate characters
    unique_chars = set(text)

    # Return the number of unique characters
    return len(unique_chars)


# Test examples
print(count_unique_characters("hello"))   # Output: 4
print(count_unique_characters("python"))  # Output: 6
print(count_unique_characters("aaa"))     # Output: 1
print(count_unique_characters("banana"))  # Output: 3
print(count_unique_characters("abcabc"))  # Output: 3
