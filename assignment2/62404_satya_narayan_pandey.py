"""
Python String Toolkit — Assignment 2
Student ID: 62404
Name: SATYA NARAYAN PANDEY

Task:
Implement unique_words(text), returning each distinct word once
while preserving the order of its first appearance.
"""


def unique_words(text):
    """Return words from text without duplicates, preserving first appearance."""
    seen = set()
    result = []

    for word in text.split():
        if word not in seen:
            result.append(word)
            seen.add(word)

    return result


if __name__ == "__main__":
    # Basic example from the assignment
    print(unique_words("red blue red"))  # ['red', 'blue']

    # Additional checks
    print(unique_words("apple banana apple orange banana"))
    print(unique_words("python"))
    print(unique_words(""))
