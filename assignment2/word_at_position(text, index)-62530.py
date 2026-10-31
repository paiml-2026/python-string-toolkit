def word_at_position(text, index):
    words = text.split()
    if 0 <= index < len(words):
        return words[index]
    else:
        return "Index out of range"

text = input("Enter any sentence")
index = int(input("Enter Index"))

print(word_at_position(text, index))
