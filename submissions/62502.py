def last_character(text):
    # Check if the string is not empty
    if len(text) > 0:
        # Return the last character of the full string
        return text[-1]
    else:
        # Return an empty string if the input is empty
        return ""

# Pass a full string containing spaces in the function call
print(last_character("Hello World"))