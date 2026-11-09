def sort_words_alphabetically(text):
  
  # Split the text into a list of words
  words_list = text.split()
  
  # Sort the list alphabetically
  words_list.sort(key=str.capitalize)

  # Print the result
  return(words_list)

# Taking input from the user
text = input()
# Calling the function and providing 'text' as argument
sort_words_alphabetically(text)

# Happy Many Apple Ola mango banana bAnana baNana
