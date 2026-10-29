def unique_words_in_first(text1, text2)
    words2 = set(text2.split())
    result = []

    for word in text1.split():
        if word not in words2 and word not in result:
            result.append(word)

    return result
