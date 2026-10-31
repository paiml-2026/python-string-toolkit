# Keep digits [ Vansh  Kapil(IT) -  62413 ]
io_str = input("Enter a string: ")

#Using filter with str
ans_str = "".join(filter(str.isdigit, io_str)) # filter(function, iteratable) 
if ans_str:
    print(ans_str)  


#Using Lambda function
ansLambdastr = "".join(filter(lambda x: x.isdigit(), io_str)) 
if ansLambdastr:
    print(ansLambdastr)

#Using Loops
ansLoopstr = ""
for char in io_str:
    if char.isdigit():
        ansLoopstr+=char
if ansLoopstr:
    print(ansLoopstr)
else:
    print("The string does ton contain any digits")
