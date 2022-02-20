def print_upper_words(words, must_start_with = set()):
    """Takes a list of words and set of letters,
    Iterates through the list of words and prints out words that begin
    with a character from set of letters as all uppercase"""
    if type(words) != list or type(must_start_with) != set:
        print("The given words or must_start_with is not a set")
        return
    for word in words:
        if type(word) == str:
            word = word.lower()
            if len(must_start_with) != 0:
                start_char = word[0]
                if start_char in must_start_with:
                    print(word.upper())
            else:
                print(word.upper())

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], must_start_with={"h", "y"})
print("\n")
print_upper_words(["cat", "dog", "bird", "fish", "cow"])