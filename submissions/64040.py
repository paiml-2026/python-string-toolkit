
# Define a function that finds the first non-repeated character
def first_non_repeated_character(text):
    
    # Loop through each character in the given text
    for char in text:
        
        # Check whether the character appears only once in the text
        if text.count(char) == 1:
            
            # Return the first character that appears only once
            return char
    
    # Return None if every character is repeated
    return None


# Store the input string in a variable
text = "aabc"

# Call the function and store the returned character
result = first_non_repeated_character(text)

# Print the first non-repeated character
print(result)
