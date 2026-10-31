def extract_words_in_quotes(text):
    """Extract text enclosed in matching double quotes.

    Example:
        extract_words_in_quotes('say "hello world" now')
        # ['hello world']
    """
    results = []
    i = 0

    while i < len(text):
        if text[i] == '"':
            start = i + 1
            end = start

            while end < len(text) and text[end] != '"':
                end += 1

            if end < len(text):
                results.append(text[start:end])
                i = end + 1
            else:
                break
        else:
            i += 1

    return results


if __name__ == "__main__":
    print(extract_words_in_quotes('say "hello world" now'))
    print(extract_words_in_quotes('She said "hi" and left'))
    print(extract_words_in_quotes('no quotes here'))
    print(extract_words_in_quotes('"first" and "second"'))
