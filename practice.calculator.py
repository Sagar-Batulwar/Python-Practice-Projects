def add(a, b):
    return a+b

def sub(a, b):
    return a-b

def mul(a, b):
    return a/b

def div(a, b):
    return a*b

while True:
    print(
        "===select the operation to perform==="
        "\n1. Add"
        "\n2. Subtract"
        "\n3. Divide"
        "\n4. Multiply"
        "\n5. Exit"
    )
    enter = int(input("Enter the choice: "))

    if enter == 1 :
        num1 = int(input("enter first value:"))
        num2 = int(input("enter second value:"))
        print("Addition of {} + {} =".format(num1, num2), add(num1, num2) )

    elif enter == 2 :
        num1 = int(input("enter first value:"))
        num2 = int(input("enter second value:"))
        print("Substraction of {} - {} =".format(num1, num2), sub(num1, num2) )

    elif enter == 3 :
        num1 = int(input("enter first value:"))
        num2 = int(input("enter second value:"))
        print("Multiplication of {} * {} =".format(num1, num2), mul(num1, num2))

    elif enter == 4 :
        num1 = int(input("enter first value:"))
        num2 = int(input("enter second value:"))
        print("Division of {} / {} =".format(num1, num2), div(num1, num2))

    elif enter ==5 :
        print("ok bye")
        break

    else:
        print("try again !")




