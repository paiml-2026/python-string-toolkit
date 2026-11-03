def find_sentence_by_word_count(text, n):
    # Store the characters of the sentence currently being checked.
    sentence = ""

    # Read the input text one character at a time.
    for char in text:
        sentence += char

        # Check for the end of a sentence.
        if char in ".!?":
            # Remove spaces around the sentence.
            sentence = sentence.strip()

            # Count whitespace-separated words.
            if len(sentence.split()) == n:
                return sentence

            # Start collecting the next sentence.
            sentence = ""

    # Check any final sentence without ending punctuation.
    sentence = sentence.strip()
    if sentence and len(sentence.split()) == n:
        return sentence

    # Return None if no sentence has exactly n words.
    return None
