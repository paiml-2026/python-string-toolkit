def words_with_repeated_letters(text):
    # This empty list will store our final answer
    result = [] 
    # Split the sentence into individual words
    words = text.split()    
    # Check each word one by one
    for word in words:   
        # Check every letter in the current word
        for letter in word: 
         # If any letter appears more than once in the word
            if word.count(letter) > 1:
                result.append(word) # Add the word to our result list
                break # Stop checking this word and move to the next one       
    return result
