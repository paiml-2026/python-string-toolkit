def most_frequent_word(text):
    # Split the input text into individual words
    words = text.split()

    # Store the frequency of each word
    frequency = {}

    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    # Find the word with the highest frequency
    most_frequent = ""

    for word in frequency:
        if most_frequent == "" or frequency[word] > frequency[most_frequent]:
            most_frequent = word

    # Return the most frequent word
    return most_frequent
