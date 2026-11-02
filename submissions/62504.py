def starts_with_vowel(text):
    """Return True if the given text starts with a vowel (a, e, i, o, u).

    The check is case-insensitive. An empty string returns False.
    """
    if not text:
        return False
    return text[0].lower() in "aeiou"


if __name__ == "__main__":
    fruit = input("Type the name of a fruit: ")
    if starts_with_vowel(fruit):
        print(f"{fruit} starts with a vowel.")
    else:
        print(f"{fruit} does not start with a vowel.")
