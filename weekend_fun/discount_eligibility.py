total_bill = float(input("Enter total bill amount: "))
is_member = input("Are you a member? (yes/no): ").lower()

if total_bill >= 1000 and is_member == "yes":
    discount = total_bill * 0.10
    final_amount = total_bill - discount
    print("10% discount applied.")
elif total_bill >= 1000:
    discount = total_bill * 0.05
    final_amount = total_bill - discount
    print("5% discount applied.")
else:
    discount = 0
    final_amount = total_bill
    print("No discount applied.")

print("Final amount to pay:", final_amount)
