def find_all_substring_position(text, sub): #defining the function

    text_len = len(text)                    #creating int variable for counting and iterating loop
    sub_len = len(sub)
    location = []

    a = text_len - sub_len + 1              #this tells us how many times we need to itereate loop

    for i in range (a):

        if sub == text[i: i+sub_len]:       #check the needed substring in the text
            location.append(i)              #appends the location if the substring is found
            

    return location                         #returns the list where the location of substring has been stored


text_string = input("Enter the string")     
sub_string = input("Enter the substring")

a = find_all_substring_position(text_string, sub_string)
print(a)

