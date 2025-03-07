
#Challenge: Create a Password Strength Checker that takes a password from the user and analyzes its strength. 💡
# 🔑 Rules:
# ✔ Weak Password: < 6 characters
# ✔ Medium Password: 6-10 characters, at least one digit
# ✔ Strong Password: > 10 characters, at least one uppercase letter, one digit, and one special character

import re
def check_password_strength(password):
    # Check for weak password
    if len(password) < 6:
        return "Weak Password"
    
    # Check for medium password
    elif 6 <= len(password) <= 10:
        if any(char.isdigit() for char in password):  # At least one digit
            return "Medium Password"
        else:
            return "Weak Password"
    
    # Check for strong password
    elif len(password) > 10:
        if (any(char.isupper() for char in password) and  # At least one uppercase letter
            any(char.isdigit() for char in password) and  # At least one digit
            any(char in "!@#$%^&*()_+[]{}|;:,.<>?/~`" for char in password)):  # At least one special character
            return "Strong Password"
        else:
            return "Medium Password"
    return "Weak Password"

# User input
password = input("Enter your password: ")
strength = check_password_strength(password)
print(f"Password Strength: {strength}")
