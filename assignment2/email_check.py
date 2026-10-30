# Import the regular expression module for pattern matching
import re

# Function to check email format
def is_valid_email_format(text):

    # Define email pattern
    pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

    # Return True if email matches the pattern, otherwise False
    return bool(re.match(pattern, text))


# Take input from user
email = input("Enter your email: ")

# Call the function and display the result
print(is_valid_email_format(email))
