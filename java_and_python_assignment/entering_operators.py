# PSEUDOCODE
# 1. Input number1
# 2. Input operator (+, -, *, /)
# 3. Input number2
# 4. Use if statements:
#       if + then add
#       if - then subtract
#       if * then multiply
#       if / then divide
# 5. Print result




num1 = float(input("Enter first number: "))
op = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if op == '+':
    print("Result:", num1 + num2)
elif op == '-':
    print("Result:", num1 - num2)
elif op == '*':
    print("Result:", num1 * num2)
elif op == '/':
    print("Result:", num1 / num2)
else:
    print("The operator is invalid")
