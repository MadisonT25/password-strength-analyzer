import re

password = input("Enter a password: ")

score = 0
feedback = []

# Common weak passwords
common_passwords = ["password", "123456", "12345678", "qwerty", "abc123"]

# Length check
if len(password) >= 8:
    score += 1
else:
    feedback.append("Use at least 8 characters")

# Uppercase check
if re.search(r"[A-Z]", password):
    score += 1
else:
    feedback.append("Add an uppercase letter")

# Lowercase check
if re.search(r"[a-z]", password):
    score += 1
else:
    feedback.append("Add a lowercase letter")

# Number check
if re.search(r"[0-9]", password):
    score += 1
else:
    feedback.append("Add a number")

# Special character check
if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
    score += 1
else:
    feedback.append("Add a special character")

# Check for common passwords
if password.lower() in common_passwords:
    feedback.append("Avoid using common passwords")
    score -= 1

# Check for repeated characters (e.g., "aaa")
if re.search(r"(.)\1\1", password):
    feedback.append("Avoid repeated characters")
    score -= 1

# Check for simple sequences
if "1234" in password or "abcd" in password.lower():
    feedback.append("Avoid predictable sequences")
    score -= 1

# Final strength rating
if score >= 5:
    print("Strength: Strong")
elif score >= 3:
    print("Strength: Moderate")
else:
    print("Strength: Weak")

# Feedback output
if feedback:
    print("\nSuggestions:")
    for item in feedback:
        print("-", item)