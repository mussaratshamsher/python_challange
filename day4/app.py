#Q: Write a Python program that takes a number as an input and converts it into words

#Solution 1

import inflect

def number_to_words(num):
    # Create an inflect engine instance
    p = inflect.engine()

    # Convert the number to words
    return p.number_to_words(num)

# Input from user
num = int(input("Enter a number: "))
print(f"Output: {number_to_words(num)}")

#Solution 2
def number_to_words(num):
    # Dictionaries for word mapping
    ones = {0: "", 1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 
            6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten", 
            11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 
            15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen"}
    
    tens = {2: "Twenty", 3: "Thirty", 4: "Forty", 5: "Fifty", 6: "Sixty", 
            7: "Seventy", 8: "Eighty", 9: "Ninety"}

    if num == 0:
        return "Zero"   
    # Helper function to handle numbers greater than 20
    def convert(number):
        if number < 20:
            return ones[number]
        elif number < 100:
            ten, one = divmod(number, 10)
            return f"{tens[ten]} {ones[one]}".strip()
        else:
            return str(number) 

    # For numbers between 0 and 99, we use the recursive helper
    return convert(num)

# Input from user
num = int(input("Enter a number: "))
print(f"Output: {number_to_words(num)}")


# Solution 3
def number_to_words(num):
    ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", 
            "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    
    tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    
    if num == 0:
        return "Zero"
    
    if 1 <= num < 20:
        return ones[num]  
          
    if 20 <= num < 100:
        ten_part = tens[num // 10]
        one_part = ones[num % 10]
        return f"{ten_part} {one_part}".strip()

# Input from user
num = int(input("Enter your number: "))
print(f"Output: {number_to_words(num)}")
