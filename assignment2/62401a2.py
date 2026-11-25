# Function to find common words in two texts
def common_words(text1, text2):

    # Split both texts into separate words
    words1 = text1.split()
    words2 = text2.split()

    # Create an empty list to store common words
    result = []

    # Check each word from the first text
    for word in words1:

        # Check if the word is present in both texts
        if word in words2 and word not in result:

            # Add the common word to the result
            result.append(word)

    # Return the list of common words
    return result


# Take input from the user
text1 = input("Enter first text: ")
text2 = input("Enter second text: ")

# Display the common words
print("Common words:", common_words(text1, text2))