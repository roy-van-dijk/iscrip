# Main class
def main():
    # Array to be checked for duplicates
    arr = [3, 9, 4, 3, 8, 7, 3, 4, 2, 1, 1]
    # Dubbels method checks for duplicates and prints them on screen

    # Find duplicates from the array with the dubbels method and print them
    print(dubbels(arr))


# Checks for duplicates and prints them on screen
def dubbels(arr):
    # Array items that have been seen
    seen = []
    # Array items that are duplicates
    duplicates = []

    # Loop through the whole array
    for a in arr:
        # If the current item has not been seen yet, add it to the seen array
        if a not in seen:
            seen.append(a)
        # If the current item HAS been seen
        else:
            # If it is not already added to the duplicates list, add it
            if a not in duplicates:
                duplicates.append(a)

    # Sorts the duplicates list and prints it
    return sorted(duplicates)

# Run the main class
if __name__ == "__main__":
    main()
