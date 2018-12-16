# Main class
def main():
    # Ask user for file input
    file = open(input())

    # File input for testing
    # file = open('/Users/royvandijk/Documents/School/iscrip/assignments_2/woordenlijst.txt')

    # Array to store the palindromes in
    palindromes = []

    # Read the file as lines
    with file as f:
        lines = f.readlines()
        # Strip whitespace and return characters like \n from the lines
        lines = [x.strip() for x in lines] 

        # Loop through each line
        for line in lines:
            # If the reversed line is equal to the original line, 
            # it is a palindrome. Add it to the palindrome list
            if line[::-1] == line:
                palindromes.append(line)

    # Join the palindromes list back separated by \n (return)
    palindromes = '\n'.join(str(palindrome) for palindrome in palindromes)

    # Print the palindromes from the list
    print(palindromes)

    # Close the file
    file.close()


# Run the main class
if __name__ == "__main__":
    main()
