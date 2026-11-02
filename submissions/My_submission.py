#Ujwal Bhan 62518
def characters_at_odd_positions(text):
    result = text[1::2]
    return result


text = input("Enter a string: ")
print("Characters at odd positions:", characters_at_odd_positions(text))