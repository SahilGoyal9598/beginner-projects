# Ask the users a bucnh of questions and if they answer correctly then we will add 1 to the total score and let's set the total limit of the questions

print("Welcome to my science quiz!")

# Input function is used to get input from the user

playing = input("Do you want to play? ")

# if else is conditinal statement where we can control the outcome based on conditions

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :")
score = 0

answer = input("Who is the king of the jungle? ")
if answer.lower() == "lion":
    print("Correct! ")
    score += 1  # it will add a score to the total score, we can change per questions marks to any integer like score += 2
else:
    print("incorrect!")

answer = input("What is our planet called? ")
if answer.lower() == "earth":
    print("Correct! ")
    score += 1
else:
    print("incorrect!")

answer = input("How many legs cow has? ")
if answer.lower() == "four":
    print("Correct! ")
    score += 1
else:
    print("incorrect!")

answer = input("Clothes are made up of? ")
if answer.lower() == "cotton":
    print("Correct! ")
    score += 1
else:
    print("incorrect!")


# Lets get the score printed
print(f"You got {score} questions correct!")
print(f"You got {score/4 * 100}% marks")
