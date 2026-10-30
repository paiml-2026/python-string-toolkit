#Generate text summary
'''"Hello world. Hello Python." → dictionary with total words, unique words, and sentence count Return a dictionary with keys total_words, unique_words, and sentence_count.'''
   

def answer(str):
  
  #for total number of words
  
  ''' strip function is important because str.split() keeps punctuation attached to words (e.g., "world." and   "world" are counted as two separate unique words, and "Hello."'''
  words = []
  for word in str.split(): #this will split the strin from wherever there is a space
      clean_word = word.strip(".,!?\"'()[]{}").lower() # Strip punctuation from words to accurately count words and unique words
      if clean_word:
            words.append(clean_word)

  total_words = len(words)

    #for number of unique words
  unique_words = len(set(words)) #this will make words a set which has an occurence of word only one time

    #for counting number of sentence
  sentence_count= str.count('.')+str.count('!')+ str.count('?')

  return {
        "total_words": total_words,
        "unique_words": unique_words,
        "sentence_count": sentence_count
    }

str= "Hello world. Hello Python."
answer= answer(str)
print(answer)

