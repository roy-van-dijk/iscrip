# Main class
def main():
    # Calculate life expectancy based on details about the 
    # by person using the levensverwachting function
    expectancy = levensverwachting(geslacht='man', roker=True, sport=2, alcohol=10, fastfood=True)

    # Print the life expectancy on screen
    print(expectancy)


# Returns life expectancy
# geslacht: Person's gender. Can be either "man" or "vrouw"
# roker: Whether the person smokes or not. Boolean
# sport: Amount of hours a week the person sports. Integer
# alcohol: Glasses of alcohol the person drinks per week. Integer 
# fastfood: Whether the person frequently consumes fastfood. Boolean
def levensverwachting(geslacht, roker, sport, alcohol, fastfood):
    # Initial life expectancy
    expectancy = 70

    # Add 4 years if the person is female
    if geslacht == "vrouw":
        expectancy += 4

    # Subtract 5 years if the person is a smoker, add 5 if not
    if roker:
        expectancy -= 5
    else:
        expectancy += 5

    # Add 1 year per hour the person sports per week.
    # Subtract 3 years if the person doesn't exercise at all
    if sport > 0:
        expectancy += sport
    else:
        expectancy -= 3

    # Subtract half a year for each drink past 7 the person consumes per week.
    # Add 2 years if the person doesn't drink at all. 
    if alcohol > 0:
        if (alcohol - 7) > 0:
            expectancy -= ((alcohol -7) * 0.5)
    else:
        expectancy += 2

    # Add 3 years if the person doesn't consume fastfood often
    if not fastfood:
        expectancy += 3

    # Round the result to 1 place after the comma and return it
    return round(expectancy, 1)


# Run the main class
if __name__ == "__main__":
    main()
