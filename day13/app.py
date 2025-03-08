

# 🚀 Challenge: Build a Simple Encryption & Decryption Tool using Python! 🔒✨
# 🔹 Task:

# 1. Take a message from the user.
# 2. Encrypt the message using a simple Caesar Cipher (shift each letter forward by 3 positions in the alphabet).
# 3. Decrypt the message back to its original form.

import string

# Encrypt using Caesar cipher with string module
def encrypt(message, shift=3):
    result = []
    for char in message:
        if char.islower():
            result.append(chr((ord(char) - ord('a') + shift) % 26 + ord('a')))
        elif char.isupper():
            result.append(chr((ord(char) - ord('A') + shift) % 26 + ord('A')))
        else:
            result.append(char)  # Non-alphabetic characters remain unchanged
    return ''.join(result)

# Decrypt the encrypted message
def decrypt(encrypted_message, shift=3):
    result = []
    for char in encrypted_message:
        if char.islower():
            result.append(chr((ord(char) - ord('a') - shift) % 26 + ord('a')))
        elif char.isupper():
            result.append(chr((ord(char) - ord('A') - shift) % 26 + ord('A')))
        else:
            result.append(char)  # Non-alphabetic characters remain unchanged
    return ''.join(result)

# Taking user input
message = input("Enter a message to encrypt: ")
encrypted_message = encrypt(message)
print(f"Encrypted Message: {encrypted_message}")

# Decrypting the message
decrypted_message = decrypt(encrypted_message)
print(f"Decrypted Message: {decrypted_message}")

