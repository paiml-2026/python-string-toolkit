#Piyush Saini, 62463, Mechanical Engineering
def anagram(s1, s2):
    if sorted(s1.lower()) == sorted(s2.lower()):
        print("They are Anagrams")
    else:
        print("They are not Anagrams")

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

anagram(str1, str2)