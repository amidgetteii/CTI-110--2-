# Alvin Midgette
# September 27, 2026
# P2HW1
# This program calculates travel expenses based on user-entered budget, gas, 
# accommodation, and food expenses, and displays the formatted results in a neat column.

def main():
    # Pseudocode:
    # 1. Prompt user to enter their budget.
    # 2. Prompt user to enter their travel destination.
    # 3. Prompt user to enter estimated amount for gas.
    # 4. Prompt user to enter estimated amount for accommodation.
    # 5. Prompt user to enter estimated amount for food.
    # 6. Add all expenses together.
    # 7. Subtract total expenses from the budget to find the remaining balance.
    # 8. Display results using formatted f-strings with a fixed-width column and 2 decimal places for money values.

    print("This program calculates and displays travel expenses\n")

    # Get inputs from the user
    budget = float(input("Enter Budget: "))
    destination = input("Enter your travel destination: ")
    gas = float(input("How much do you think you will spend on gas? "))
    accommodation = float(input("Approximately, how much will you need for accommodation/hotel? "))
    food = float(input("Last, how much do you need for food? "))

    # Calculate total expenses and remaining balance
    total_expenses = gas + accommodation + food
    remaining_balance = budget - total_expenses

    # Display formatted output
    print("\n------------Travel Expenses------------")
    print(f"{'Location:':<20} {destination}")
    print(f"{'Initial Budget:':<20} ${budget:.2f}")
    print(f"{'Fuel:':<20} ${gas:.2f}")
    print(f"{'Accommodations:':<20} ${accommodation:.2f}")
    print(f"{'Food:':<20} ${food:.2f}")
    print("---------------------------------------")
    print(f"{'Remaining Balance:':<20} ${remaining_balance:.2f}")

if __name__ == "__main__":
    main()