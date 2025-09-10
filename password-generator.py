import random

letters = ''' a b cd e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z '''.split()
numbers = ''' 0 1 2 3 4 5 6 7 8 9 '''.split()
symbols = ''' ! @ # $ % & * '''.split()

password = [
    random.choice(letters),
    random.choice(numbers),
    random.choice(symbols)
]

allChars = letters + numbers + symbols
length = int(input("Enter the length of pw you wanna generate: "))
passwordLength = length



password += random.choices(allChars, k = passwordLength - 3)

password = "".join(password)
print(password)