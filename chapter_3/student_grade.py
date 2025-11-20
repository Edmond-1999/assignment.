user_grade_input = input("Enter grade from 0 to 100: ")
if user_grade_input.isdigit():
    numeric_grade = float(user_grade_input)
    if numeric_grade >= 90:
        print("A")
    elif numeric_grade >= 80:
        print("B")
    elif numeric_grade >= 70:
        print("C")
    elif numeric_grade >= 60:
        print("D")
    else:
        print("F")
else:
    print("Invalid grade")
