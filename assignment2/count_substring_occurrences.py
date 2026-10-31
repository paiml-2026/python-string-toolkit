def count_substring_occurrences(text, sub):
    # Check if the substring is empty
    if sub == "":
        return 0

    # Count the number of occurrences of sub in text
    count = 0

    # Check each possible position in the text
    for i in range(len(text) - len(sub) + 1):
        # Compare the substring starting at index i
        if text[i:i + len(sub)] == sub:
            count += 1

    # Return the total number of occurrences
    return count
