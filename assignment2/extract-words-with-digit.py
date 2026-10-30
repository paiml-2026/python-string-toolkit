# Program to extract words with digit from a string or text
def extract(text):
    words = text.split(" ")  #convert string into a iterable list 
    
    res = []  # result stored in list
    for ch in words:  #iterating over a word in a list

        hasalpha = False
        hasnum = False

        for c in ch:  # iteration over every alphabet in word

            if (c.isalpha()):  #if alphabet is present in word
                hasalpha = True

            if c.isdigit():     #if digit is present in the same word
                hasnum = True

        if hasalpha and hasnum: #if both variables are true then stored the word in result
            res.append(ch)
    return res