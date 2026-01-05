#DISCLAIMER:CREDIT UNIT OR GRADE POINT DOESN'T ACCEPT LETTERS!!Please use digits.

def score_to_grade_point(score): 
    if score >= 70 and score <= 100:
        return 5.0
    elif score >= 60:
        return 4.0
    elif score >= 50:
        return 3.0
    elif score >= 45:
        return 2.0
    elif score >= 40:
        return 1.0
    else:
        return 0.0


while True:  

    total_quality_points = 0
    total_credit_units = 0    

    while True:
        try:
            courses_offered = int(input("Enter the number of courses you offered this semester: "))
        except ValueError:
            print("Number of courses can't be in words, please use digits.")
            continue

        if courses_offered > 0 and courses_offered <= 15:
            break
        else:
            print("Number of courses too low/high.Please enter a number ranging from 1-15 ") 


    for num in range(courses_offered):

        while True:
            try:
                score = int(input(f"Enter your score for course {num+1}: "))
            except ValueError:
                print("Score can't be in words, please enter digits.")
                continue

            if score > 0 and score <= 100:
                break
            else:
                print("Invalid score,please enter a value ranging between 1 and 100")

        while True:        
            try:
                credit_unit = int(input(f"Enter the credit unit for course {num+1}: "))
            except ValueError:
                print("Credit unit can't be in words, please enter digits.")
                continue

            if credit_unit > 0 and credit_unit <= 18:
                break
            
            else:
                print("Invalid credit unit,credit unit too low/high." \
                "Credit must be greater than ZERO(0) and less than EIGHTEEN(18)")

        grade_point = score_to_grade_point(score)
        quality_point = grade_point * credit_unit

        total_quality_points += quality_point
        total_credit_units += credit_unit


    gpa = total_quality_points / total_credit_units

    print("\nCURRENT SEMESTER RESULT")
    print("Total credit unit:", total_credit_units)
    print("Total quality point:", total_quality_points)
    print("Your GPA is:", round(gpa, 3))
    while True:
        choice = input("\nDo you want to calculate another GPA? (yes/no): ").lower()
        
        if choice == "yes":
            print("OK!")
            break
        elif choice == "no":
            print("Good Bye!")
            exit()
        else:
            print("Please type either (yes/no) ")



#WILL ANSWER QUESTIONS BUT PREFER NOT TO BE ASKED.LOL