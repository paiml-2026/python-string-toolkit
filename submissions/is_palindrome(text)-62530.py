def is_palindrome(text):              # Define a function to check for a palindrome
    text = str(text)                  # Convert the input into a string
    return text == text[::-1]         # Compare the string with its reverse and return True or False


print(is_palindrome("madam"))         # Output: True
print(is_palindrome("hello"))         # Output: False
