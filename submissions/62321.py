def count_consonants(text):
    count = 0  # start counting from zero

    # check each character in the text
    for ch in text:
        if ch.isalpha() and ch.lower() not in "aeiou":
            count += 1  # count the consonant

    return count  # return total consonants
