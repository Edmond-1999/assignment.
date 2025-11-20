total_pass = 0
total_fail = 0
student_number = 1
while student_number <= 10:
    user_input = input("Enter result for student " + str(student_number) + " (1 for pass, 2 for fail): ")
    if user_input == "1":
        total_pass = total_pass + 1
        student_number = student_number + 1
    elif user_input == "2":
        total_fail = total_fail + 1
        student_number = student_number + 1
    else:
        print("Enter only 1 or 2")
print("Passes:", total_pass)
print("Failures:", total_fail)
if total_pass > 8:
    print("Bonus to instructor")
