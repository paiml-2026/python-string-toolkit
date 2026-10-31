def truncate_text(text, limit):
    # Check if the text length exceeds the given limit
    if len(text) > limit:

        # Keep the characters up to limit - 3
        # to make space for three dots
        return text[:limit - 3] + "..."

    # If the text is within the limit, return it unchanged
    return text
