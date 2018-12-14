# Main class
def main():
    print(T9('aanbod'))

    print(GSMoniemen('aanbod', 'bamboe'))

    print(GSMoniemen('maandag', 'vrijdag'))


# Returns T9 key dialing sequence of a given word
def T9(word):
    # Key layout on a T9 keyboard stored as an array
    keys = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
    # Transform given word to lowercase
    word = word.lower()
    # Initialise combination string to be filled by the sequence
    combination = ""
    # Index will be the physical number key to be pressed by the user
    # Starts at 2 because the array above stars at 0 AND the T9 keys
    # start with 'abc' at key number 2
    index = 2

    # Loop through each letter in the given word
    for letter in word:
        # Loop through each key in the keys array
        for key in keys:
            # If the current letter is inside of the key
            if letter in key:
                # Add the current index (physical number key) to the
                # result sequence
                combination += str(index)
            # If the current letter is not in this key, add 1 to the
            # index (key to be pressed)
            index += 1
        # After this letter has been checked, reset index back to 2
        index = 2

    # Return the T9 sequence
    return combination


# Returns True if both given words have the same T9 dialing sequence,
# returns False if not
def GSMoniemen(word1, word2):
    return T9(word1) == T9(word2)

# Run the main class
if __name__ == "__main__":
    main()
