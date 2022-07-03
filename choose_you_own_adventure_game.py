name = input("Type your name: ")
print(f"Welcome! {name} to this adventure!")


def not_a_valid():
    print("not a valid option")


answer = input(
    "You're on a dirt road, it has come to an end nad you can go left or right. Which way would you like to go? > "
).lower()

if answer == "left":
    answer = input(
        "You come to a river, you can walk around it or swim accross? Type walk to walk around and swim to swim accross >  "
    ).lower()

    if answer == "swim":
        print("You swim accross and were eaton by an allegator. ")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game")
    else:
        not_a_valid()

elif answer == "right":
    answer = input(
        "You come to a bridge, it looks woobly. Do you want to cross it or go back > "
    ).lower()

    if answer == "back":
        print("You go back and loose")
    elif answer == "cross":
        answer = input(
            "YOu crossed the bridge and meet a stranger. Do you want to talk to them? >  "
        ).lower()

        if answer == "yes":
            print("You talk to the stranger and they give you gold. You WIN!")
        elif answer == "no":
            print("You ignored the stranger and they are offended and you LOOSE!")
        else:
            not_a_valid()

    else:
        not_a_valid()

else:
    not_a_valid()


print(f"Thanks for trying {name}")
