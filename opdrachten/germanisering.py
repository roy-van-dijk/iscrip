# Main class
def main():
    # Original sentence
    sentence = "Geluk helpt soms, moed altijd."
    # Capitalize words with germaniseer() function
    sentence = germaniseer(sentence)
    # Print the capitalized sentence
    print(sentence)


# Capitalizes each word in a sentence
def germaniseer(sentence):
    # Separator defines where words can be split out of a sentence
    separator = " "
    # Store each word from the sentenece in the words array
    words = sentence.split(separator)
    # New capitalized words will be stored in this newWords array
    new_words = []

    # Loop through all words in the array
    for word in words: 
        # Capitalize a word
        new_word = word.capitalize()
        # Store the word in the newWord array
        new_words.append(new_word)

    # Join the newWords array back into a string and return it
    return separator.join(new_words)


# Run the main class
if __name__ == "__main__":
    main()
