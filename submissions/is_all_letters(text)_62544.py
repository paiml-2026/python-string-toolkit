


# creating a function is_all_letters()

text = "Python"

def is_all_letters(text) :          #defining the function

 for ch in text:                    #applying for loop 
   if not ch.isalpha():             #checking the text string for alphabets
     return False                   # false if incorrect
   
 return True                        #true if correct
print(is_all_letters(text))         #calling the function
