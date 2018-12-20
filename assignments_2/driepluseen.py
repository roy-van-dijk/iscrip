# Main class
def main():
    # Intial list with prices of items to be bought
    prijzen = [3.23, 5.32, 8.23, 2.23, 9.98, 7.43, 6.43, 8.23, 4.23]

    # Print total price of all items together minus the 2 cheapest items
    print(samen(prijzen))

    # Print prices array grouped in 4's
    print(groeperen(prijzen))

    # Print result if going through checkout multiple times
    print(gegroepeerd(prijzen))

    # Print the difference
    print(winst(prijzen))


# Returns total price of all items together minus the 2 cheapest items
def samen(items):
    # Sort the list from high to low prices
    items = sorted(items, reverse=True)

    # Every 4th item is free, so divide the length of the array by 4 and
    # that is amount of items to be removed
    items_to_remove = len(items) - round(len(items) / 4)

    # Slice last x items off the original list
    items = items[:items_to_remove]

    # Return the sum of the new items list, rounded to 2 decimal places
    return round(sum(items), 2)


# Returns prices array grouped in 4's
def groeperen(items):
    # Sort the list from high to low prices
    items = sorted(items, reverse=True)

    # List of tuples to be filled
    tuple_items = []

    # Amount of full tuples we will need is the length of the items in the
    # list divided by 4
    tuple_count = round(len(items) / 4)

    # The leftover items in the last tuple e.g.:
    # 9 items divided by 4 = 1 left over in the last tuple
    leftover_count = len(items) % 4

    # Make a tuple from the last leftover items
    leftover_tuple = tuple(items[-leftover_count:])

    # Loop through the amount of tuples we will need
    for i in range(tuple_count):
        # Make a new tuple from the first 4 items in the list
        tup = tuple(items[:4])
        # Add the new tuple to the tuple list
        tuple_items.append(tup)
        # Slice the first 4 items from the original items list
        items = items[4:]

    # Add the leftover tuple created earlier to the end of the tuple list
    tuple_items.append(leftover_tuple)

    # Return the tuple list
    return tuple_items


# Returns result if going through checkout multiple times
def gegroepeerd(items):
    # Total price to be calculated
    total = 0
    # Get the list groups with our groeperen function
    groups = groeperen(items)

    # For every group
    for group in groups:
        # Calculate the sum of that group minus the cheapest
        # item and add it to the total
        total += sum(group[:3])

    # Return the total, round to 2 decimal places
    return round(total, 2)


# Returns the difference
def winst(items):
    # Return the difference between the 2 approaches,
    # round to 2 decimal places
    return round(samen(items) - gegroepeerd(items), 2)


# Run the main class
if __name__ == "__main__":
    main()
