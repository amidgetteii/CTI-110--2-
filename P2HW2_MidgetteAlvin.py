# Your Name
# September 27, 2026
# P2HW2
# This program asks the user for six module test grades, stores them in a list,
# calculates the lowest grade, highest grade, sum of grades, and average grade, 
# and displays the results formatted nicely.

def main():
    # Pseudocode:
    # 1. Prompt the user for module 1 grade and convert to float.
    # 2. Prompt the user for module 2 grade and convert to float.
    # 3. Prompt the user for module 3 grade and convert to float.
    # 4. Prompt the user for module 4 grade and convert to float.
    # 5. Prompt the user for module 5 grade and convert to float.
    # 6. Prompt the user for module 6 grade and convert to float.
    # 7. Store all six grades into a descriptive list called module_grades.
    # 8. Find the lowest grade using min() function.
    # 9. Find the highest grade using max() function.
    # 10. Calculate the sum of the grades using sum() function.
    # 11. Calculate the average by dividing the sum by the length of the list (6).
    # 12. Display all calculated results with clear headings and proper formatting.

    # Prompt user for test grades
    mod1 = float(input("Enter grade for Module 1: "))
    mod2 = float(input("Enter grade for Module 2: "))
    mod3 = float(input("Enter grade for Module 3: "))
    mod4 = float(input("Enter grade for Module 4: "))
    mod5 = float(input("Enter grade for Module 5: "))
    mod6 = float(input("Enter grade for Module 6: "))

    # Store grades in a descriptive list
    module_grades = [mod1, mod2, mod3, mod4, mod5, mod6]

    # Calculate required results using built-in list functions (no loops or if statements)
    lowest_grade = min(module_grades)
    highest_grade = max(module_grades)
    sum_grades = sum(module_grades)
    average_grades = sum_grades / len(module_grades)

    # Display results
    print("\n------------Results------------")
    print(f"Lowest Grade:       {lowest_grade:.1f}")
    print(f"Highest Grade:      {highest_grade:.1f}")
    print(f"Sum of Grades:      {sum_grades:.1f}")
    print(f"Average:            {average_grades:.2f}")
    print("--------------------------------")

if __name__ == "__main__":
    main()