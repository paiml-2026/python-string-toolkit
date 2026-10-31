def count_lowercase(text):
    count = 0  # start counting from zero

    # check each character in the text
    for ch in text:
        if ch.islower():  # check if the character is lowercase
            count += 1  # increase the count

    return count  # return the total lowercase letters
