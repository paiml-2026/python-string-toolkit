def count_special_characters(text):
    special_characters = "!@#$%^&*()_+-=[]{}|;:',.<>?/~`"
    #mentioning all the special characters

    count = 0 #declaring to count the number of special characters

    #in string handling ch in text in a simpler practice than using for i in range(len(text))
    for ch in text:
        if ch in special_characters:
            count += 1
    return count

print("Number of special characters:", count_special_characters(text))
