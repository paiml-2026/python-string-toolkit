def words_ending_with(text, suffix):
    # Split the text into individual words
    words = text.split()

    # Create an empty list to store matching words
    result = []

    # Check each word one by one
    for word in words:

        # Check if the word ends with the given suffix
        if word.endswith(suffix):

            # Add the matching word to the result list
            result.append(word)

    # Return the list of matching words
    return result


# Example input
text = "walking talked running"
suffix = "ing"

# Call the function and print the result
print(words_ending_with(text, suffix))