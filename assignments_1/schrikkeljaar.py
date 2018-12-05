# Main class
def main():
    # Input year to be checked
    year = input("Enter a year:")
    # Convert year to integer
    year = int(year)
    # Print whether year is leap or not
    print_leap_year(year)


# Prints leap year or not leap year based on provided year
def print_leap_year(year):
    # Check if year is leap year
    if is_leap_year(year):
        # Print leap year text
        print("schrikkeljaar")
    else:
        # Print no leap year text
        print("geen schrikkeljaar")


# Checks whether year is leap or not
def is_leap_year(year):
    # If the year mod 4 results in no remainder and year mod 400
    # results in no remainder (definition of a leap year)
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


# Run the main class
if __name__ == "__main__":
    main()
