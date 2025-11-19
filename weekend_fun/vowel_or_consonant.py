letter = input("Enter a letter: ").lower()

if len(letter) != 1 or not letter.isalpha():
    print("Invalid input")
elif letter in ("a", "e", "i", "o", "u"):
    print("Vowel")
else:
    print("Consonant")
