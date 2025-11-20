total_numbers = input("How many numbers will you enter: ")
if not total_numbers.isdigit():
    print("Invalid amount")
    exit()
total_numbers = int(total_numbers)
running_total = 0
number_counter = 1
while number_counter <= total_numbers:
    user_value = input("Enter number " + str(number_counter) + ": ")
    try:
        numeric_value = float(user_value)
        running_total = running_total + numeric_value
        number_counter = number_counter + 1
    except:
        print("Invalid number, try again")
print("Total:", running_total)
