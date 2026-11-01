def convert_snake_to_camel(text):
    words = text.split("_")  #split text into words using underscore 
    result = words[0]  #Start with the first word
    for word in words[1:]:  #go through the remaining words
        word = word.capitalize()  #capitalize the first letter of the remaining word
        result = result + word  #add the capitalized word to the result
    return result  #return final camelcase text