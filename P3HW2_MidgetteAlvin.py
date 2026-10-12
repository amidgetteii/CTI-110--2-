# CTI-110
# P3HW2 - Salary Calculator
# Alvin Midgette
# 10/11/2026
# This program calculates an employee's gross pay, including regular pay and overtime pay (if hours worked exceed 40).

# Pseudocode:
# 1. Prompt user to enter employee name, hours worked, and pay rate.
# 2. Check if hours worked > 40 (overtime condition).
# 3. IF hours > 40:
#        Calculate overtime hours = hours worked - 40
#        Calculate regular hours = 40
#        Calculate overtime pay = overtime hours * (pay rate * 1.5)
#        Calculate regular pay = 40 * pay rate
#    ELSE:
#        Overtime hours = 0
#        Overtime pay = 0.0
#        Regular hours = hours worked
#        Regular pay = regular hours * pay rate
# 4. Calculate gross pay = regular pay + overtime pay
# 5. Display employee details, hours, pay breakdown, and gross pay formatted nicely.

def main():
    # Input section
    emp_name = input("Enter employee's name: ")
    hours_worked = float(input("Enter number of hours worked: "))
    pay_rate = float(input("Enter employee's pay rate: "))
    
    print("-" * 35)

    # Decision structure for overtime calculation
    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        reg_hours = 40.0
        reg_pay = reg_hours * pay_rate
        ot_pay = overtime_hours * (pay_rate * 1.5)
    else:
        overtime_hours = 0.0
        reg_hours = hours_worked
        reg_pay = reg_hours * pay_rate
        ot_pay = 0.0

    # Total gross pay
    gross_pay = reg_pay + ot_pay

    # Output section
    print(f"Employee name:     {emp_name}\n")
    print(f"{'Hours Worked':<15}{'Pay Rate':<12}{'OverTime':<12}{'OT Pay':<12}{'RegHourPay':<15}{'Gross Pay':<12}")
    print("-" * 75)
    print(f"{hours_worked:<15.1f}{pay_rate:<12.2f}{overtime_hours:<12.1f}{ot_pay:<12.2f}{reg_pay:<15.2f}{gross_pay:<12.2f}")

if __name__ == "__main__":
    main()