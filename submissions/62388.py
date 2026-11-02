def count_lines(text):
    """
    Returns the number of lines in the given string.
    Returns 0 when string is empty.
    """
    if not text:
        return 0
    return len(text.splitlines())  #splits text at new line


print(count_lines("one\ntwo\nthree"))  # Expected: 3
print(count_lines("hello world"))       # Expected: 1
print(count_lines(""))                  # Expected: 0