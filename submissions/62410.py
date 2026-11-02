def capitalise_words(sentence):
    words = sentence.split()   #converts the sentence into a list of words
    for i in range(len(words)):   #traversing over the list 'words'
        words[i] = words[i][0].upper() + words[i][1 : ]   #capitalising the first letter of every word of the list 
    return " ".join(words)   #joining the words 