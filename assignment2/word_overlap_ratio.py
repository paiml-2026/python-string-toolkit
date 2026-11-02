def word_overlap_ratio(text1, text2):
    """
    Calculate the word overlap ratio between two texts
    using Jaccard similarity.

    Formula:
    Jaccard Similarity = Common Unique Words / Total Unique Words
    """

    # Convert text to lowercase and split it into words.
    # This makes the comparison case-insensitive.
    words1 = text1.lower().split()
    words2 = text2.lower().split()

    # Convert lists to sets to remove duplicate words.
    set1 = set(words1)
    set2 = set(words2)

    # Find the number of words common to both texts.
    common_words = set1.intersection(set2)

    # Find all unique words present in either text.
    all_words = set1.union(set2)

    # Handle the case where both texts contain no words.
    if len(all_words) == 0:
        return 0.0

    # Calculate the word overlap ratio.
    ratio = len(common_words) / len(all_words)

    return ratio


# Main program: accept any two texts from the user.
if __name__ == "__main__":
    text1 = input("Enter the first text: ")
    text2 = input("Enter the second text: ")

    # Call the function and display the result.
    result = word_overlap_ratio(text1, text2)

    print("Word Overlap Ratio:", round(result, 4))
