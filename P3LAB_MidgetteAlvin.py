# CTI-110
# P3LAB - Simple Change
# Midgette Alvin
# 10/11/2026

def main():
    # Get money amount from user as a float
    user_input = float(input("Enter an amount of money as a float: $"))
    print(f"Change amount: {user_input}")

    # Convert money into an integer to avoid floating-point math inaccuracies
    change = int(round(user_input * 100))
    print(f"Integer change value: {change}")

    # Calculate the most efficient number of dollars, quarters, dimes, nickels, and pennies
    num_dollars = change // 100
    change = change - (num_dollars * 100)

    num_quarters = change // 25
    change = change - (num_quarters * 25)

    num_dimes = change // 10
    change = change - (num_dimes * 10)

    num_nickels = change // 5
    change = change - (num_nickels * 5)

    num_pennies = change

    # Display the results using appropriate singular/plural forms and omitting 0-quantity coins/dollars.
    
    # Dollars output
    if num_dollars > 0:
        if num_dollars == 1:
            print(f"{num_dollars} dollar")
        else:
            print(f"{num_dollars} dollars")

    # Quarters output
    if num_quarters > 0:
        if num_quarters == 1:
            print(f"{num_quarters} quarter")
        else:
            print(f"{num_quarters} quarters")

    # Dimes output
    if num_dimes > 0:
        if num_dimes == 1:
            print(f"{num_dimes} dime")
        else:
            print(f"{num_dimes} dimes")

    # Nickels output
    if num_nickels > 0:
        if num_nickels == 1:
            print(f"{num_nickels} nickel")
        else:
            print(f"{num_nickels} nickels")

    # Pennies output
    if num_pennies > 0:
        if num_pennies == 1:
            print(f"{num_pennies} penny")
        else:
            print(f"{num_pennies} pennies")

if __name__ == "__main__":
    main()
