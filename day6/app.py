
#Q: Write a Python program that takes a number as a user input , converts it into binary form &
#    checks wether it is palindrome or not a palindrome.

def check_palindrome_binary(num):
    # Converts the integer to binary (without the '0b' prefix)
    binary_rep = bin(num)[2:]

    # Checks if the binary representation is a palindrome
    if binary_rep == binary_rep[::-1]:
        print(f"Binary: {binary_rep}")
        print("Output: Palindrome ✅")
    else:
        print(f"Binary: {binary_rep}")
        print("Output: Not a Palindrome ❌")

# Taking user input
num = int(input("Enter an integer: "))
check_palindrome_binary(num)