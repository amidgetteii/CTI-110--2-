# CTI-110
# P3HW1 - Debugging
# Midgette Alvin
# 10/11/2026
# This program takes 6 number grades, determines the lowest, highest, sum, average, and displays the letter grade.

# Enter grades for six modules
mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# Add grades entered to a list
grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

# Determine lowest, highest, sum, and average for grades
low = min(grades)
high = max(grades)
total_sum = sum(grades)
avg = total_sum / len(grades)

# Display results
print("\n------------Results------------")
print(f"Lowest Grade:  {low}")
print(f"Highest Grade: {high}")
print(f"Sum of Grades: {total_sum}")
print(f"Average:       {avg:.2f}")
print("-" * 31)

# Determine letter grade for average
if avg >= 90:
    print('Your grade is: A')
elif avg >= 80:
    print('Your grade is: B')
elif avg >= 70:
    print('Your grade is: C')
elif avg >= 60:
    print('Your grade is: D')
else:
    print('Your grade is: F')