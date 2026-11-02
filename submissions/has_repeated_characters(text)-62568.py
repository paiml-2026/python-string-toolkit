# Function to check whether the string contains repeated characters
def has_repeated_characters(text):
    a=text   # Store the input string in variable a
    a=a.lower() # Convert the entire string into lowercase
    a=a.replace(" ","")  # Remove all spaces from the string

    # Traverse each character of the string
    for i in range(len(a)):
        # Check whether the character is an alphabet
        if a[i].isalpha():
             # Compare the current character with the following characters
            for j in range(i+1,len(a)):
                # Check whether the characters are same
                if a[i]==a[j]:
                    return True  # Return True if a repeated character is found

    return False # Return False if no repeated character is found

# Accept a string from the user
text=input("Enter a string:")

# Call the function and check its return value
if has_repeated_characters(text):
    print("True")  # Display True if a repeated character exists

else:
    print("False")  # Display False if no repeated character exists


    
