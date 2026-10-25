# Name: Alvin Midgette
# Date: October 25, 2026
# Assignment Name: P4HW2 - Salary Calculator for Multiple Employees
# Description: This program calculates regular pay, overtime pay, and gross 
#              pay for multiple employees using a sentinel loop ("Done"), and 
#              displays the cumulative totals for all employees when finished.

# PSEUDOCODE:
# 1. Initialize accumulator variables for totals:
#    - total_employees = 0
#    - total_overtime_pay = 0.0
#    - total_regular_pay = 0.0
#    - total_gross_pay = 0.0
# 2. Ask the user to enter the employee's name or "Done" to terminate (Sentinel Loop prime).
# 3. START WHILE LOOP (while employee_name is not equal to "Done"):
#    a. Ask for the employee's pay rate.
#    b. Ask for the number of hours worked.
#    c. Check if hours worked > 40:
#       - IF hours > 40:
#         * regular_hours = 40
#         * overtime_hours = hours - 40
#         * regular_pay = regular_hours * pay_rate
#         * overtime_pay = overtime_hours * pay_rate * 1.5
#       - ELSE:
#         * regular_hours = hours
#         * overtime_hours = 0.0
#         * regular_pay = regular_hours * pay_rate
#         * overtime_pay = 0.0
#    d. Calculate gross_pay = regular_pay + overtime_pay.
#    e. Display individual employee breakdown (Hours, Pay Rate, Overtime, Reg Pay, Gross Pay).
#    f. Add values to running totals (total_employees, total_overtime_pay, total_regular_pay, total_gross_pay).
#    g. Prompt for the next employee's name or "Done" to continue/exit loop.
# 4. After loop terminates (when user enters "Done"):
#    a. Display total number of employees entered.
#    b. Display total overtime pay for all employees.
#    c. Display total regular pay for all employees.
#    d. Display total gross pay for all employees.

def main():
    # Initialize totals accumulators
    total_employees = 0
    total_overtime_pay = 0.0
    total_regular_pay = 0.0
    total_gross_pay = 0.0
    
    # Prime the sentinel loop
    emp_name = input("Enter employee's name or \"Done\" to terminate: ")
    
    while emp_name != "Done":
        # 1. Ask for pay rate and hours worked
        pay_rate = float(input(f"Enter employee's pay rate: "))
        hours_worked = float(input(f"Enter number of hours worked: "))
        
        # 2. Calculate overtime and regular pay
        if hours_worked > 40:
            regular_hours = 40
            overtime_hours = hours_worked - 40
            regular_pay = regular_hours * pay_rate
            overtime_pay = overtime_hours * pay_rate * 1.5
        else:
            regular_hours = hours_worked
            overtime_hours = 0.0
            regular_pay = regular_hours * pay_rate
            overtime_pay = 0.0
            
        gross_pay = regular_pay + overtime_pay
        
        # Display individual employee results
        print("\n-------------------------------------------------")
        print(f"Employee name: {emp_name}")
        print(f"Hours Worked: {hours_worked}")
        print(f"Pay Rate: ${pay_rate:.2f}")
        print(f"Overtime Hours: {overtime_hours}")
        print(f"Overtime Pay: ${overtime_pay:.2f}")
        print(f"Regular Hour Pay: ${regular_pay:.2f}")
        print(f"Gross Pay: ${gross_pay:.2f}")
        print("-------------------------------------------------\n")
        
        # Accumulate totals
        total_employees += 1
        total_overtime_pay += overtime_pay
        total_regular_pay += regular_pay
        total_gross_pay += gross_pay
        
        # Prompt for next employee name (sentinel condition check)
        emp_name = input("Enter employee's name or \"Done\" to terminate: ")
        
    # Display final grand totals after "Done" is entered
    print("\n=================================================")
    print(f"Total number of employees entered: {total_employees}")
    print(f"Total overtime pay for all employees: ${total_overtime_pay:.2f}")
    print(f"Total regular pay for all employees: ${total_regular_pay:.2f}")
    print(f"Total gross pay for all employees: ${total_gross_pay:.2f}")
    print("=================================================")

if __name__ == "__main__":
    main()
