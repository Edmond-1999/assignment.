age = int(input("Enter your age: "))

max_heart_rate = 220 - age
target_lower = 0.5 * max_heart_rate
target_upper = 0.85 * max_heart_rate

print("Your maximum heart rate is:", max_heart_rate, "bpm")
print("Your target heart rate range is:", target_lower, "to", target_upper, "bpm")
