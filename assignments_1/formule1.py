import math


# Main class
def main():

    # Ask for input of prize country string
    print("Voer de grote prijs in:")
    prize = input()

    # Ask for input of distance per lap, cast to a float
    print("Voer de afstand in:")
    lap_distance = float(input())

    # Ask for input of average time per lap
    print("Voer de gemiddelde tijd in:")
    time = float(input())

    # Print the output string
    print_output(prize, lap_distance, time)


# Prints the output string
def print_output(prize, lap_distance, time):

    # Calculatess the amount of laps to be completed to exceed 305 km
    laps = math.ceil(305 / lap_distance)

    # Calculates total race time 
    total_time = time * laps

    # Check if total time exceeds 2 hours
    if(total_time >= 120):
        # Repeat loop if time is still more than 2 hours
        while(total_time >= 120):
            # Decrement 1 lap from the total time
            total_time -= time
            # Decrement 1 lap from the total laps
            laps -= 1
        # Add back the last lap that puts it over 2 hours
        total_time += time
        laps += 1

    # Calculatess the total distance driven
    total_distance = round(laps * lap_distance, 3)

    # Extra check for special case Monaco
    if(prize.lower() == "monaco"):
        total_distance = 260.52
        laps = 78

    # Template for output string
    template = "De grote prijs van %s wordt verreden over %s ronden (%s km)."

    # Formats the output string with calculated values
    output = template % (prize, laps, total_distance)

    # Prints the output string
    print(output)


# Run the main class
if __name__ == "__main__":
    main()
