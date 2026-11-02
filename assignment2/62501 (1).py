
def convert_camel_to_snake(text):
    # Add an underscore before every uppercase letter
    result = ""

    for char in text:
        if char.isupper():
            result += "_" + char.lower()
        else:
            result += char

    # Remove the first underscore if it exists
    if result.startswith("_"):
        result = result[1:]

    return result


# Test cases
print(convert_camel_to_snake("helloWorld"))
print(convert_camel_to_snake("myVariableName"))
print(convert_camel_to_snake("studentName"))