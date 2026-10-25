# -------------------------------------------------------------
# Name: Alvin Midgette
# Date: October 25, 2026
# Assignment Name: P4LAB2 - Multiplication Table
# Description: This program prompts the user for an integer, checks if 
#              it is positive or negative, displays its multiplication 
#              table from 1 to 12 if positive/zero, and uses a while loop 
#              to allow the user to run the program again.
# -------------------------------------------------------------

# PSEUDOCODE:
# 1. Initialize keep_running variable to "yes" to control the program loop.
# 2. START WHILE LOOP (while keep_running equals "yes"):
#    a. Input Step: Ask the user to enter an integer and store it.
#    b. Decision Step (Positive vs. Negative):
#       - IF integer >= 0:
#         * Multiplication Table Logic: Use a FOR loop from 1 to 12 
#           to calculate and print the product of the integer and the loop counter.
#       - ELSE (integer < 0):
#         * Print a message stating that negative values are not accepted.
#    c. Repeat/Run-again Logic: Ask the user if they want to run the program again ("yes" or "no").
#    d. Update keep_running with the user's response.
# 3. Program Exit Condition: The loop terminates when the user enters "no".

def main():
    # While loop to control repeating the program
    keep_running = "yes"
    
    while keep_running == "yes":
        # 1. Ask the user to enter an integer
        user_num = int(input("Enter an integer: "))
        
        # 2 & 3. Decision for positive vs. negative integer
        if user_num >= 0:
            # For loop to display multiplication table from 1 to 12
            for i in range(1, 13):
                product = user_num * i
                print(f"{user_num} * {i} = {product}")
        else:
            print("Negative values are not accepted.")
            
        # 4. Ask the user if they want to run the program again
        keep_running = input("Would you like to run the program again? (yes/no): ").strip().lower()

if __name__ == "__main__":
    main()
