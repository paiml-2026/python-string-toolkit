def most_frequent_character(text):
    """Return the most frequent character."""
    count_value = []
    max_char = ""

    for char in text:
        count = text.count(char)
        count_value.append(count)

        if count > max(count_value[:-1], default=0): #If two char have same frequency then the first one will be return.
            max_char = char

    return max_char


text = input("Enter the text: ")
print(f"The most frequent char is: {most_frequent_character(text)}")
