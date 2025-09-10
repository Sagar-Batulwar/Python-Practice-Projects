import random

choice = ["rock", "paper", "scissors"]

computer = random.choice(choice)

valid_choices = ["rock", "paper", "scissors"]
user = input("Enter your guess: ").lower()

while user not in valid_choices:
    print("invalid choice ! please only enter rock, paper, or scissors")
    user = input("Enter your guess: ").lower()


print(f'Your guess is: {user}')
print(f'Computer guess is: {computer}')

if user == computer :
    print("its a tie")
elif (user == "paper" and computer == "rock") or \
    (user == "scissors" and computer == "paper") or \
    (user == "rock" and computer == "scissors") :
    print("user win")
else : print("computer wins")



