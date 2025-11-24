passes = 0
fails = 0

for number_of_people in range(1, 16):
    score = int(input(f"Enter score for student {number_of_people}: "))

    if score >= 45:
        passes += 1
    else:
        fails += 1

print("Number of students that passed:", passes)
print("Number of students that failed:", fails)
