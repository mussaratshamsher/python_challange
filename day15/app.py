import random
import string

def generate_password(length):
    if length < 8:
        print("Password length should be at least 8 characters for security.")
        return None

    # Define the characters to choose from
    all_characters = string.ascii_letters + string.digits + string.punctuation
    
    # Randomly choose characters from the list
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password

def main():
    length = int(input("Enter the desired password length: "))
    password = generate_password(length)
    
    if password:
        print(f"Your generated password is: {password}")

if __name__ == "__main__":
    main()
