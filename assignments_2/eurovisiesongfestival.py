# Main class
def main():
    # Initial scoreboard dictionary
    example_scorebord = {}

    # Scores from UK
    UK = {
            'Lithuania': 7,
            'Russia': 3,
            'Estonia': 4,
            'Azerbaijan': 2,
            'Sweden': 12,
            'Turkey': 1,
            'Spain': 8,
            'Germany': 6,
            'Malta': 5,
            'Ireland': 10
    }

    # Add scores from UK to the above dictionary
    scoresToevoegen(example_scorebord, UK)
    # Print the current scoreboard in its entirety
    print(scoresTonen(example_scorebord))

    # Scores from HU
    HU = {
            'Albania': 8,
            'Russia': 7,
            'Iceland': 6,
            'Italy': 5,
            'Sweden': 12,
            'Turkey': 3,
            'Spain': 1,
            'Germany': 10,
            'Serbia': 4,
            'Moldova': 2
    }

    # Add scores from HU to the above dictionary
    scoresToevoegen(example_scorebord, HU)
    # Print the top 3 from the scoreboard
    print(scoresTonen(example_scorebord, 3))


# Adds scores from a country to the scoreboard
def scoresToevoegen(scorebord, scores_country):
    # Loop through each item in the country's scores
    for key, value in scores_country.items():
        # If the country has already been added to the scoreboard
        if key in scorebord:
            # Calculate the new value of the country's score
            new_value = (scorebord[key] + value)
            # Overwrite the old score with the new value
            scorebord[key] = new_value
        # If the country is not on the scoreboard yet, create a new entry
        else:
            scorebord[key] = value


# Returns the scoreboard sorted by score and alphabetically
# Optional parameter n declares the amount of scores to be returned
def scoresTonen(scorebord, n=-1):
    # Empty results array to be filled with tuples
    results = []

    # Loop through each item in the scoreboard
    for key, value in scorebord.items():
        # Tuple with the country name as the key and its score as the value
        tuple = (key, value)
        # Add the tuple to the results array
        results.append(tuple)

    # Sort the results array alphabetically 
    results.sort(key=lambda tup: tup[0])
    # Sort the results array again by score
    results.sort(key=lambda tup: tup[1], reverse=True)

    # Return n entries of the results array
    return results[:n]


# Run the main class
if __name__ == "__main__":
    main()
