def remove_duplicates(s: str) -> str:
    """
    Remove duplicate characters from a string, keeping only the
    first occurrence of each character and preserving order.

    Example:
        "banana" -> "ban"

    Time complexity:  O(n), one pass through the string
    Space complexity: O(k), where k = number of unique characters
    """
    seen = set()      # Tracks characters we've already encountered
    result = []       # Collects characters to keep (list is faster than string concatenation)

    for ch in s:
        if ch not in seen:       # First time seeing this character
            seen.add(ch)         # Mark it as seen
            result.append(ch)    # Keep it in the output
        # Otherwise: duplicate, so skip it

    return "".join(result)       # Combine the kept characters into a string


# --- Test cases ---
if __name__ == "__main__":
    print(remove_duplicates("banana"))   # ban
    print(remove_duplicates("hello"))    # helo
    print(remove_duplicates("aaaa"))     # a
    print(remove_duplicates(""))         # (empty string)
    print(remove_duplicates("Aa"))       # Aa  (case-sensitive)