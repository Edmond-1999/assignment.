# PSEUDOCODE
# 1. Input year
# 2. A year is leap if:
#       divisible by 4
#       AND NOT divisible by 100
#       EXCEPT if divisible by 400  (leap)
# 3. Print whether leap or not




year = int(input("Enter year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")
