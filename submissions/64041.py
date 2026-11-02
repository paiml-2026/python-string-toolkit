# Function to count each character in a string
def character_frequency(text):
    frequency = {}  # Store each character and its count

    # Check each character in the given text
    for character in text:
        if character in frequency:
            frequency[character] += 1  # Increase count
        else:
            frequency[character] = 1  # Add new character

    return frequency  # Return the dictionary


# Take input from the user
text = input("Enter a string: ")

# Call the function and display the result
result = character_frequency(text)
print("Character frequency:", result)
