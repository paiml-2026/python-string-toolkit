def find_sentence_by_word_count(text, n):
  #stores the characters of the text currently being checked.
  sentence = ""

#Read the input text one character at a time.
for char in text:
  sentence += char

    if char in ".!?":
      #Removes spaces at the beginning or at the end of the sentence
      sentence = sentence.strip()

        #splits the sentence into whitespaced-separated words
        if len(sentence.split()) == n:
          return sentence

        #starts collecting the next sentence
        sentence = ""

#Check any final sentence that does not end with punctuation.
sentence = sentence.strip()
if sentence and len(sentence.split()) == n:
  return sentence

#return none if no sentence has exactly n words
return none
