def group_words_by_first_letter(words):
    groups = {}

    for word in words:
        first_letter = word[0].lower()

        if first_letter not in groups:
            groups[first_letter] = []

        groups[first_letter].append(word)

    return groups


try:
    print(group_words_by_first_letter(["apple", "ant", "ball"]))
    print(group_words_by_first_letter(["Apple", "Ant", "Ball", "Banana", "Cat"]))
    print(group_words_by_first_letter(["dog", "deer", "elephant", "Duck"]))

except Exception as e:
    print("An error occurred:", e)
