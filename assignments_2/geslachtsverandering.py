import string


# Main class
def main():
    # Original translations array
    vertalingen = {'hij': 'zij', 'broer': 'zus'}
    # Example of vertaal function usage
    print(vertaal('HIJ', vertalingen))
    # Exmaple of geslachtsverandering function usage
    print(geslachtsverandering('Hij is mijn broer.', vertalingen))
    # Exmaple of geslachtsherstel function usage
    print(geslachtsherstel('Zij is mijn zus.', vertalingen))


# Translates a given word if it is included in the given dictionary.
# Returns word unchange if not
def vertaal(word, dictionary):
    # Loop through each item in the dictionary
    for key, value in dictionary.items():
        # If the given word is found in the dictionary as a key
        if word.lower() in key.lower():
            # If the word is in all caps, return the translation in all caps
            if word.isupper():
                return value.upper()
            # If the first letter is uppercase,
            # return the first letter as uppercase
            if word[0].isupper():
                return value.capitalize()
            # If neither, return the word as all lowercase
            return value.lower()

    # Return word unchanged if it is not in the dictionary
    return word


# Replaces each occurence of a dictionary entry in a sentence with its
# corresponding value
def geslachtsverandering(sentence, dictionary):
    # Remove punctuation from sentence
    translator = sentence.maketrans('', '', string.punctuation)
    stripped = sentence.translate(translator)

    # Sentence words array
    sentence_words = stripped.split(" ")

    # For each word in the sentence array
    for old_word in sentence_words:
        # Translate the word using the vertaal function
        new_word = vertaal(old_word, dictionary)
        # Replace the word with the translated word
        sentence = sentence.replace(old_word, new_word)

    # Return the new translated sentence
    return sentence


# Reverts translated sentence back into the original
def geslachtsherstel(sentence, dictionary):
    # Reverse the dictionary
    reversed_dictionary = {v: k for k, v in dictionary.items()}
    # Return the geslachtsverandering with the reversed dictionary
    return geslachtsverandering(sentence, reversed_dictionary)


if __name__ == "__main__":
    main()
