import random

low = int(input("Enter lower Bound = "))
high = int(input("Enter higher Bound = "))

print("you have only 7 chances to guess the integer")

num = random.randint(low, high)
count = 0

while count < 7:
    count += 1
    guess = int(input("enter your guess: "))
    if guess == num:
        print(f"congratulation the {num} is a correct guess you did it in {count} try!")
        break
    elif count >= 7 and guess != num:
        print("No ..your limit is exausted. try gain Later")
    elif guess > num:
        print("Too high ! Enter lower number")
    elif guess < num:
        print("Too low ! Enter Lower number")
