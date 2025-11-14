# PSEUDOCODE
# 1. Get father's age
# 2. Get son's age
# 3. Compute difference in ages → father_age - son_age
# 4. The father is twice as old when:
#       father_age - years = 2 * (son_age - years)
#   OR in the future:
#       father_age + years = 2 * (son_age + years)
# 5. Solve: years = father_age - 2*son_age
# 6. Print the number of years



father = int(input("Enter father's age: "))
son = int(input("Enter son's age: "))

years = abs(father - 2 * son)

print("Years difference:", years)
