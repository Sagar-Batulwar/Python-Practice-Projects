import random
print("guess the bike brand name")
print("you have 10 chances")

bikes = ["honda", "hero", "bajaj", "tvs", "yamaha", "suzuki"]

bike = random.choice(bikes)

chance = 10

entered = ''

while chance > 0:
    chance -= 1
    remain = 0
    for word in bike:
        if word in entered:
            print(word)
        else :
            print("_")
            remain += 1

    print()        
    enter = input("Enter a letter to guess: ")
    entered += enter
    
    print()
    if remain == 0 :
        print("You win. Good Luck")
        break
    else: print("try again you have", chance,"chances left")



    
