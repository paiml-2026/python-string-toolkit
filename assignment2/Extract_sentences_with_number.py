import re

def extract_sentences_with_number(text):
    sentences = re.split(r'[.!?]', text)
    result = []

    for sentence in sentences:
        if re.search(r'\d+', sentence):
            result.append(sentence.strip())

    return result


text = "I am 21 years old. I study ECE. I have 2 brothers. Python is easy."

print(extract_sentences_with_number(text))
