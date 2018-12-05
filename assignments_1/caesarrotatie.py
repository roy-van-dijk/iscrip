# Main class
def main():
    # Ask user to input amount to decode by
    print("Enter amount to rotate by:")
    rotation_amount = input()

    # Ask user for encoded string
    print("Enter sentence to rotate:")
    rotation_sentence = input()

    # Print decoded string
    print(decode(rotation_amount, rotation_sentence))


# Rotates a string. 
# amount = places to rotate
# sentence = string to rotate
# direction = direction of the rotation. True = forward, False = backward
def rotate(amount, sentence, direction):
    # Entire alphabet string
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    # Rotated sentence to be constructed
    new_sentence = ""

    # Loop through each letter in the given sentence
    for letter in sentence:
        is_upper = False
        # Check whether this letter is uppercase and lowercase it if so
        if letter.isupper():
            letter = letter.lower()
            is_upper = True

        # Rotation direction based on direction parameter
        if direction:
            new_letter_position = alphabet.find(letter) + amount
        else:
            new_letter_position = alphabet.find(letter) - amount

        # If a letter is in fact a letter from the alphabet
        if letter in alphabet:
            # Adds the new letter to the new_sentence string
            # If the letter was uppercase, transform it back to uppercase
            if is_upper:
                new_sentence += alphabet[new_letter_position].upper()
            else:
                new_sentence += alphabet[new_letter_position]
        # If it is not in the alphabet (punctuation), add it without any change
        else:
            new_sentence += letter

    # Return the new sentence
    return new_sentence


# Decodes a string (direction = backward)
def decode(amount, sentence):
    return rotate(int(amount), sentence, False)


# Encodes a string (direction = forward)
def encode(amount, sentence):
    return rotate(int(amount), sentence, True)


# Run the main class
if __name__ == "__main__":
    main()
