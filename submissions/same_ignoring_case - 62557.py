def same_ignoring_case(a, b):
    return a.lower() == b.lower()


a = input("Enter the first string: ")
b = input("Enter the second string: ")

if a.isalpha() and b.isalpha():
    print(same_ignoring_case(a, b))
else:
    print("Invalid input! Please enter alphabetical values only.")
