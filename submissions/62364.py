# ASSIGNMENT01: count the character in a text

def count_character(text, ch):
    count = 0         #variable that count the frequency of character
    for c in text:   #iterating over given text
        if c == ch:  #comparison of characters
            count+=1
    return count
