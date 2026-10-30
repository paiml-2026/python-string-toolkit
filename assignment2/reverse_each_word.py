def reverse_each_word(text):
    # Split the text into words
    words = text.split()
    result = []
    # Reverse each word
    for word in words:
        result.append(word[::-1])
    # Join all reversed words
    return " ".join(result)
