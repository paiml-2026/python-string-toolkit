def is_alphanumeric(text):                          #Defining the function
    
    if not text.isalnum():                          # Check if the string consists only of letters and numbers
        return False
        
    has_letters = not text.isdigit()                # Check that it isn't purely numbers
    has_numbers = not text.isalpha()                # Check that it isn't purely letters
    
    return has_letters and has_numbers              # Checks if both condition and return true if both are true


test_string = input("Enter your string")            # We take our test input/string

returned_value = is_alphanumeric(test_string)       # Passing it through the function

print(returned_value)                               # Print the value the function have returned
    
