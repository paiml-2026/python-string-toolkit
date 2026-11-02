def count_spaces(text):
    count = 0  # start counting from zero

    # go through each character in the text
    for ch in text:
        if ch == " ":  # check if it is a space
            count += 1  # increase the count by one

    return count  # return the total spaces
