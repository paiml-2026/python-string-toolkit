def is_all_digits(text):
    if text == "":
        return False

    for ch in text:
        if ch < "0" or ch > "9":
            return False

    return True
