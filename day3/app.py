

#  Write a Python program that take a number as a user input & checks wether it is Prime number
#  or not a Prime number.

def is_prime(num):  
    if num <= 1:  
        return False  
    for i in range(2, int(num**0.5) + 1):  
        if num % i == 0:  
            return False  
    return True  

# User Input  
try:  
    user_input = int(input("Enter a number: "))  
    if is_prime(user_input):  
        print(f"{user_input} is a prime number.")  
    else:  
        print(f"{user_input} is not a prime number.")  
except ValueError:  
    print("Please enter a valid integer.")