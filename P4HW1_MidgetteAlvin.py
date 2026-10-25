# Name: Alvin Midgette
# Date: October 25, 2026
# Assignment Name: P4HW1 - Score List and Average
# Description: This program collects a specified number of scores, validates each 
#              score to ensure it is between 0 and 100, drops the lowest score, 
#              calculates the average of the remaining scores, determines the 
#              letter grade, and displays the results.

# PSEUDOCODE:
# 1. Initialize an empty list named score_list to store entered scores.
# 2. Ask the user how many scores they would like to enter.
# 3. Use a FOR loop to iterate through the specified number of scores:
#    a. Prompt the user to enter a score.
#    b. Use a WHILE loop (validation loop) to check if the score is between 0 and 100:
#       - If invalid, print an error message and ask for a valid score again.
#    c. Once valid, append the score to score_list.
# 4. After collecting all scores:
#    a. Find the lowest score in score_list using min().
#    b. Create a copy of the list and remove the lowest score from it.
#    c. Calculate the average of the scores in the modified list.
#    d. Determine the letter grade based on the calculated average (A, B, C, D, F).
#    e. Display the lowest score, modified score list, average, and letter grade.

def main():
    # Initialize score list
    score_list = []
    
    # Ask user to input the number of scores they would like to enter
    num_scores = int(input("How many scores would you like to enter? "))
    
    # Create a loop to collect the number of scores
    for i in range(1, num_scores + 1):
        score = float(input(f"Enter score #{i}: "))
        
        # Validation loop: check if score is between 0 and 100
        while score < 0 or score > 100:
            print("\nINVALID score entered!!!!")
            print("Score should be between 0 and 100.")
            score = float(input(f"Enter valid score #{i} again: "))
        
        # Add valid score to the list
        score_list.append(score)
        
    print("\n-----------------Results-----------------")
    
    # Find lowest score entered
    lowest_score = min(score_list)
    print(f"Lowest score : {lowest_score}")
    
    # Create modified list after dropping lowest score
    modified_list = list(score_list)
    modified_list.remove(lowest_score)
    print(f"Modified list: {modified_list}")
    
    # Calculate the average of scores in the modified list
    if len(modified_list) > 0:
        average = sum(modified_list) / len(modified_list)
    else:
        average = 0.0
    print(f"Scores Average: {average:.2f}")
    
    # Determine the letter grade for the calculated average
    if average >= 90:
        letter_grade = 'A'
    elif average >= 80:
        letter_grade = 'B'
    elif average >= 70:
        letter_grade = 'C'
    elif average >= 60:
        letter_grade = 'D'
    else:
        letter_grade = 'F'
        
    print(f"Grade        : {letter_grade}")
    print("-----------------------------------------")

if __name__ == "__main__":
    main()
