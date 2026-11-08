def longest_sentence(text):
    # Split the text into individual sentences
    sentences = text.split('.')

    # Remove extra spaces and empty sentences
    sentences = [s.strip() for s in sentences if s.strip()]

    # Find the sentence containing the maximum number of words
    longest = max(sentences, key=lambda s: len(s.split()))

    # Return the longest sentence
    return longest


# Example
text = "I am here. Python is very useful."

# Call the function and print the result
print(longest_sentence(text))
