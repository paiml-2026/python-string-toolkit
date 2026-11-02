def sort_words_by_length(text):
    words = text.split()
    return sorted(words, key=len)
