# 62518 - Ujwal Bhan 
# Activity2 - Count the number of words in each sentence a in given string
def sentence_word_counts(text):
    """
    Return the word count for each sentence in order.
    """
    sentences = text.split(".")

    result = []

    for sentence in sentences:
        words = sentence.split()

        if words:
            result.append(len(words))

    return result

if __name__ == "__main__":
    print(sentence_word_counts("Hello there👋"))
    print(sentence_word_counts("I am Ujwal Bhan from Jammu🔫. My Id is 6518"))
    print(sentence_word_counts("I love coding❤️. Python is great."))
    print(sentence_word_counts("I like Python.🐍"))
    print(sentence_word_counts(""))