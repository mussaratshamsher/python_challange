import random

print("🎨📌 Welcome to number Guessing Game!")
print("💭 You have 5 chances to guess the number between 50 & 100.")

#module to guess number
number_to_guess = random.randrange(50, 100)

chances = 5

guess_counter = 0

#loop on the basis of chances
while guess_counter < chances:
    guess_counter += 1  # incrementing the guess counter on each attempt
    my_guess = int(input("✍\tPlease enter your number➡ : "))

    #conditions on the basis of guessed number
    if my_guess == number_to_guess:
        print(f"The number is {number_to_guess} & you found it right! in the {guess_counter} attempt")
        break
    elif guess_counter >= chances and my_guess != number_to_guess:       
        print(f"Oops sorry, the number is {number_to_guess}, better luck next time.")
        break

    elif my_guess < number_to_guess:
        print("Your guessed number is low, try again!")

    elif my_guess > number_to_guess:
        print("Your guessed number is higher, try again!")
