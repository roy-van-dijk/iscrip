# Main class
def main():
    # Ask user to input the amount of numbers they wish to check
    print("Enter the amount of numbers (1-50):")
    amount = int(input())

    # Check if number is between 1 and 50, otherwise ask again
    while amount < 1 or amount > 50:
        print("Number not in range of 1-50. Try again:")
        amount = int(input())

    # Numbers array to store inputs in
    numbers = []

    # Based on the amount of numbers they wish to input,
    # ask for that amount of inputs
    for i in range(amount):
        print("Enter number " + str(i) + " (1-100):")
        number = int(input())

        # Check if number is between 1 and 100, otherwise ask again
        while amount < 1 or amount > 100:
            print("Number not in range of 1-100. Try again:")
            number = int(input())

        # Add the inputted number to the numbers array
        numbers.append(number)

    # Use the calc function to calculate the
    # result for each inputted number and print it
    print("")
    for number in numbers:
        print(calc(number))


# Returns an integer based on passed variable n where the returned integer
# is a multiple of n and the integer is equal to the sum of the digits in n
def calc(n):
    # Number to loop through, increments by n each iteration as the result
    # Always has to be a multiple of n
    i = n
    # Infinite loop
    while(True):
        # Number will add up to the sum of each digit in n e.g. 23
        # converts to 5 (2 + 3)
        added_up = 0
        # Loops through i (current iteration of outer loop) as a string
        for ii in str(i):
            # Adds the current iteration of the inner loop to
            # the added_up variable
            added_up += int(ii)
        # If the total added up value equals n (our original number),
        # we have found our number
        if(added_up == n):
            return i
        # Increment i by the value of n
        i += n


# Run the main class
if __name__ == "__main__":
    main()
