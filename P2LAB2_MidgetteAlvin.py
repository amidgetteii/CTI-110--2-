# Alvin Midgette
# September 27, 2026
# P2LAB2
# This program creates a dictionary of vehicles and their MPG,
# prompts the user to select a vehicle, calculates gas needed based on miles driven,
# and displays the formatted result.

def main():
    # Pseudocode:
    # 1. Create a dictionary mapping vehicles (keys) to their MPG (values).
    # 2. Get all the keys from the dictionary and display them.
    # 3. Prompt the user to enter one of the vehicles.
    # 4. Look up and display the MPG for the entered vehicle.
    # 5. Prompt the user to enter the number of miles they will drive.
    # 6. Calculate the gallons of gas needed (miles driven / mpg).
    # 7. Display the result rounded to two decimal places using an f-string.

    # Step 1: Create the dictionary with vehicles and their MPG
    vehicles = {
        "Camaro": 18.21,
        "Prius": 52.36,
        "Model S": 110,
        "Silverado": 26
    }

    # Step 2: Create a variable that holds all the keys and print it
    keys = vehicles.keys()
    print(list(keys))

    # Step 3: Prompt the user to enter a vehicle
    car_name = input("\nEnter a vehicle from the dictionary: ")

    # Step 4: Display the MPG for the selected vehicle
    car_mpg = vehicles[car_name]
    print(f"\n{car_name} gets {car_mpg} miles per gallon.")

    # Step 5: Prompt the user to enter the number of miles they will drive
    miles_driven = float(input(f"How many miles will you drive the {car_name}? "))

    # Step 6: Calculate the gallons of gas needed
    gallons_needed = miles_driven / car_mpg

    # Step 7: Display the gallons of gas needed rounded to two decimal places
    print(f"\n{gallons_needed:.2f} gallon(s) of gas are needed to drive the {car_name} {miles_driven} miles.")

if __name__ == "__main__":
    main()