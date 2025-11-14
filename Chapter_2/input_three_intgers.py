a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))
c = int(input("Enter third integer: "))

sum_of_numbers = a + b + c
average = sum_of_numbers / 3
product = a * b * c

smallest = min(a, b, c)
largest = max(a, b, c)

print("Sum:", sum_of_numbers)
print("Average:", average)
print("Product:", product)
print("Smallest:", smallest)
print("Largest:", largest)
