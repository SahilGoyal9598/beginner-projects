# let's play rock/paper/scissors

import random

options = ["rock", "paper", "scissor"]

user_win = 0
comp_win = 0

while True:
    user_input = input(f"Choose from {options} or Q is you want to quit > ").lower()
    if user_input == "q":
        break
    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    # 0: rock, 1: paper, 2: scissors

    comp_pick = options[random_number]
    print(f"computer choose {comp_pick}.")

    if user_input == "rock" and comp_pick == "scissor":
        print("You won!")
        user_win += 1

    elif user_input == "paper" and comp_pick == "rock":
        print("You won!")
        user_win += 1

    elif user_input == "scissors" and comp_pick == "paper":
        print("you won!")
        user_win += 1

    else:
        print("You lost")
        comp_win += 1

    if user_win > comp_win:
        print(f"you won {user_win} times as compare to the computer's {comp_win}")
    else:
        print(f"The computer won {comp_win} times as compare to your's {user_win}")

print("Goodbye! ")
