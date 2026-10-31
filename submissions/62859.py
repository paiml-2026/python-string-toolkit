def freq_count(s):
    freq = {}
    for word in s.split(','):
        freq[word] = freq.get(word, 0) + 1
    return freq

print(freq_count("hi,hi,bye"))
