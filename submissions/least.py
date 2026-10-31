def least_frequent_char(text: str):
    if not text:
        return None
        
    # Step 1: Count character frequencies manually
    frequencies = {}
    for char in text:
        frequencies[char] = frequencies.get(char, 0) + 1
        
    # Step 2: Find the character with the minimum frequency
    return min(frequencies, key=frequencies.get)

# Example usage:
text = input()
print(least_frequent_char(text))  # Output: f
