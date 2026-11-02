def first_repeated_character(text):
    seen_characters = set()

    for character in text:
        if character in seen_characters:
            return character
        seen_characters.add(character)

    return None
