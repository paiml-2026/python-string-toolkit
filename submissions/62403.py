# Thus function replaces vowels with a entered special character
def replace_vowels(text, symbol):
    vowels = "aeiouAEIOU"
    result = ""

    for char in text:
        if char in vowels:
            result += symbol
        else:
            result += char
    return result

print(replace_vowels("hello", "*"))
print(replace_vowels("Saniya" , "#"))
print(replace_vowels("Welcome to Python !"  , "*"))
print(replace_vowels("Pnktr" , "%"))