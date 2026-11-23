
def reverse_word_order(text):
    """
    Reverse the order of words in a given sentence
    without reversing the individual letters.

    Example:
    Input:  "I like Python"
    Output: "Python like I"
    """

    # Step 1: Split the sentence into individual words
    words = text.split()

    # Step 2: Reverse the order of words using slicing
    reversed_words = words[::-1]

    # Step 3: Join the reversed words into a single string
    result = " ".join(reversed_words)

    # Step 4: Return the reversed sentence
    return result


# Test the function with an example
sentence = "I like Python"

# Call the function and store the result
output = reverse_word_order(sentence)

# Display the original and reversed sentences
print("Original sentence:", sentence)
print("Reversed sentence:", output)
