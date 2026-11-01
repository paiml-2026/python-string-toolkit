def extract_uppercase_words(text):
    words=text.split()
    uppercase=[]
    for word in words:
        if word.isupper():
            uppercase.append(word)

    return uppercase