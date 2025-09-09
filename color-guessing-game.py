import random

name = input("whats your name? ")

print("hey player", name,"!")
print("guess the color: ")

colors = ['red', 'pink', 'green', 'yellow', 'blue', 'violet']
color = random.choice(colors)

guesses = ''
tries = 12

while tries > 0 :
    tries -= 1

    remaining  = 0

    for char in color:
        if char in guesses:
            print(char)
        else :
            print("_")
            remaining += 1

    if remaining == 0:
        print("congratulation you won")
        print("the color is: ", color)
        break

    guess = input("guess the color: ")
    
    guesses += guess

    if guess == color:
        print(f'congratulations the color is {color}')
    else:
        print(f"try again you have {tries} turns left")