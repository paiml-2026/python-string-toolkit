def remove_digits(text):
    result = ""
    for char in text:
        if not char.isdigit():
            result += char
    return result

text = input("Enter some text: ")
print("Text without digits:", remove_digits(text))