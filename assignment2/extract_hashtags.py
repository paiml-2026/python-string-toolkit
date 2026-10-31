def extract_hashtags(text):
    hashtags = []
    for word in text.split():
        if len(word) > 1 and word[0] == '#' and (word[1].isalnum() or word[1] == '_'):
            hashtags.append(word)
                
    return hashtags