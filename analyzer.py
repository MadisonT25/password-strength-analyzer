import re

password = input("Enter a password: ")

score = 0
feedback = []

if len(password) >= 8:
    score += 1
else:
    feedback.append("At least 8 characters")

if re.search(r"[A-Z]", password):
    score += 1
else:
    feedback.append("Add uppercase letter")

if re.search(r"[a-z]", password):
    score += 1
else:
    feedback.append("Add lowercase letter")

if re.search(r"[0-9]", password):
    score += 1
else:
    feedback.append("Add a number")

if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
    score += 1
else:
    feedback.append("Add a special character")

if score == 5:
    print("Strength: Strong")
elif score >= 3:
    print("Strength: Moderate")
else:
    print("Strength: Weak")

if feedback:
    print("Suggestions:")
    for item in feedback:
        print("-", item)
    