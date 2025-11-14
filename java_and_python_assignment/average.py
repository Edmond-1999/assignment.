# PSEUDOCODE
# 1. Input 3 scores
# 2. Compute average = (score1 + score2 + score3) / 3
# 3. If average between 90 and 100  (A)
#    If between 80 and 89  (B)
#    If between 70 and 79  (C)
#    If between 60 and 69  (D)
#    If less than 60  (F)
# 4. Print letter grade




score1 = int(input("Enter score 1: "))
score2 = int(input("Enter score 2: "))
score3 = int(input("Enter score 3: "))

avg = (score1 + score2 + score3) / 3

if 90 <= avg <= 100:
    grade = 'A'
elif 80 <= avg < 90:
    grade = 'B'
elif 70 <= avg < 80:
    grade = 'C'
elif 60 <= avg < 70:
    grade = 'D'
else:
    grade = 'F'

print("Average:", avg)
print("Grade:", grade)
