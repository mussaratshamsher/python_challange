# 🚀 Challenge: "Password Strength Checker" 🔐
# Create a password strength checker! You need to write a Python program that analyzes the strength of a password 
# provided by the user and determines whether the password is weak, moderate, or strong! 💪🔑
# 🔥 Requirements:
# ⿡ Take the password input from the user.
# ⿢ Check the strength of the password:

# Weak: If the password is shorter than 6 characters or only contains alphabets.
# Moderate: If the password is 8 or more characters long but lacks special characters.
# Strong: If the password is 8 or more characters long and contains uppercase letters, lowercase letters, numbers, and special characters.
# ⿣ Inform the user about the strength category of their password.

# Solution:

import re  # Import the regular expression module

def check_password_strength(password):
    # Check for weak password
    if len(password) < 6 or password.isalpha():
        return "Weak ❌"
    
    # Check for moderate password
    if len(password) >= 8 and not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return "Moderate ⚠"
    
    # Check for strong password
    if (len(password) >= 8 and 
        re.search(r'[A-Z]', password) and 
        re.search(r'[a-z]', password) and 
        re.search(r'[0-9]', password) and 
        re.search(r'[!@#$%^&*(),.?":{}|<>]', password)):
        return "Strong ✅"
    
    # If no condition is met
    return "Weak ❌"

# Get password input from user
password = input("Enter your password: ")

# Output the password strength
print("Password Strength:", check_password_strength(password))
