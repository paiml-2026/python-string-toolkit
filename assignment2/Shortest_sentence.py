import re

def shortest_sentence(text):
    if not text.strip():
        return ""

    sentences = re.split(r'(?<=[.!?])\s+', text.strip())

    shortest = min(sentences, key=lambda s: len(s.split()))

    return shortest


text = "I am here. Go now."
print(shortest_sentence(text))
