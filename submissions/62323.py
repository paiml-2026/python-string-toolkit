#Function to count the number of digits in a given string
def count_digits(text):  
    count = 0

    for d in text:
        if d in '0123456789':  #Checks wether a digit is present or not
            count += 1  #Counts the number of digits

    return count
