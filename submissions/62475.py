def swap_first_last(text):
    # Return as it is if length is less than 2
    if len(text) < 2:
        return text

    # Swap first and last characters
    return text[-1] + text[1:-1] + text[0]

# Example
print(swap_first_last("hello"))  # oellh