# define a function named is_acronym having 'text' and 'acronym' as parameters
def is_acronym(text, candidate):
  # define variable s and store the first letter of the phrase
  s = text[0]
  # loop through every position of text; i goes from 0 up to the last index
  for i in range(0, len(text)):
      if (text[i]== ' '):
         s = s + text[i+1]
  j=0
  # check if s and candidate have different lengths
  if (len(s)!=len(candidate)):
    print('False')
  else:
      # loop through each position of s
      for i in range(0, len(s)):
         if (candidate[i].lower()==s[i].lower()):
            j= j+1
      if (j==len(s)):
          print('True')
      else:
          print('False')

text, candidate = input(), input()
# call the function with the two inputs
is_acronym(text, candidate)
