def remove_word(text, target):
    words = text.split()
    result = []

    for word in words:
        if word != target:
            result.append(word)

    return " ".join(result)


text = input("Enter a sentence: ")
target = input("Enter word to remove: ")

print(remove_word(text, target))
