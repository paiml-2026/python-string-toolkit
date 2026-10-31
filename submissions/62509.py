#Function to extract initials from a full name

def extract_initials(text):
    #Remove extra space from beginning and end
    text = text.strip()

    #Check whether the input text is empty
    if not text:
        return "No name provided"

    #Split the full name into individual words
    words = text.split()

    #Create an empty string to store the initials
    initials = ""

    #Traverse through each word in the name
    for word in words:
        #extract the first character and convert it to upper case
        first_letter = word[0].upper()

        #Add the initialsto the result
        initials = initials + first_letter

    #Return the final initials
    return initials
