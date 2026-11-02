def expand_repeated_characters(text):
    result = ""
    i = 0

    while i < len(text):
        letter = text[i]          # current letter
        i += 1

        count = ""                # collect digits after the letter
        while i < len(text) and text[i].isdigit():
            count += text[i]
            i += 1

        if count:                 # a number followed the letter
            result += letter * int(count)
        else:                     # no number: keep the letter once
            result += letter

    return result


print(expand_repeated_characters("a3b2"))    # aaabb
print(expand_repeated_characters("x1y4z2"))  # xyyyyzz
print(expand_repeated_characters("a10"))     # aaaaaaaaaa