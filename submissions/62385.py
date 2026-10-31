def longest_word_length(text):
    # Split the string into a list of words based on spaces
    words = text.split()
    
    max_length = 0
    
    # Check the length of each word
    for word in words:
        current_length = len(word)
        if current_length > max_length:
            max_length = current_length
            
    return max_length

# Example usage:
sentence = " I like Python"
print(longest_word_length(sentence))  # Output: 6
