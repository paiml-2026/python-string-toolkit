# Define a function to compare two strings, ignoring case differences
def same_ignoring_case(a, b):
    return a.lower() == b.lower()


# Take two strings as input from the user
a = input("Enter the first string: ")
b = input("Enter the second string: ")

# Check whether both inputs contain only alphabetical characters
if a.isalpha() and b.isalpha():
    # Compare the strings without considering uppercase or lowercase
    print(same_ignoring_case(a, b))
else:
    # Display an error message if either input is invalid
    print("Invalid input! Please enter alphabetical values only.")
