# Function to remove vowels from the text
def remove_vowels(text):

    # Create an empty string to store the result
    result = ""

    # Check each character one by one
    for ch in text:

        # If the character is not a vowel, add it to result
        if ch not in "aeiouAEIOU":
            result = result + ch

    # Return the final string
    return result


# Take input from the user
text = input("Enter a text: ")

# Call the function and display the result
print("Original text:", text)
print("After removing vowels:", remove_vowels(text))