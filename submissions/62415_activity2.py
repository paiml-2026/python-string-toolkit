def remove_duplicate_words(text):
    seen = set()
    result = []

    for word in text.split():
        if word not in seen:
            seen.add(word)
            result.append(word)

    return " ".join(result)


print(remove_duplicate_words("red blue red green blue")) # red blue green
