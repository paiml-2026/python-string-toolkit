def sentences_with_keyword(text, keyword):
    result = []

    # Split text into sentences at each period
    for sentence in text.split("."):
        sentence = sentence.strip()

        # Keep the sentence if it contains the keyword (ignoring case)
        if sentence != "" and keyword.lower() in sentence.lower():
            result.append(sentence + ".")

    return result


# Test
print(sentences_with_keyword("Python is easy. Java is popular.", "Python"))
# Output: ['Python is easy.']