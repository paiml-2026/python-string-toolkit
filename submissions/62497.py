# To find the longest word in a sentence.
def longest_word(sentence):
    words = sentence.split()
    longest = words[0]
    for word in words:
        if len(word)> len(longest):
            longest = word
    return longest
print(longest_word("i like python"))



