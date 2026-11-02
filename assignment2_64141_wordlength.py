
def word_length(words):
    d = {}
    for word in words:
        length = len(word)
        d[length] = d.get(length, 0) + 1
    return d

words = input("Enter words separated by spaces: ").split()

print(word_length(words))
