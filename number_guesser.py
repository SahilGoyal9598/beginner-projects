# number guessing game

import random

user_input_number = input("Upto where do you do you want to guess: ")

if user_input_number.isdigit():
    user_input_number = int(user_input_number)
else:
    print("Please enter a number next time")
    quit()


random_number = random.randint(0, user_input_number)
guesses = 0


while True:
    guesses += 1
    user_guess = input("make a guess > ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time")
        continue

    if user_guess == random_number:
        print("Congraulation! you got it right")
        break
    elif user_guess > random_number:
        print("You're guessing too high")
    else:
        print("You're guessing too low")

print(f"You got the right answer in {guesses} guesses")
