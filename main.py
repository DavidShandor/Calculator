import tkinter

def add(a,b):
    return a+b

def mult(a,b):
    return a*b

def divide(a,b):
    return a/b

def substract(a,b):
    return a-b

print("Welcome to my calculator program!")
while True:
    print("Please chooce an opertion:")
    print("1. Add")
    print("2. Substract")
    print("3. Divide")
    print("4. Multiply")
    print("5. exit")


    user_opt = input()
    if user_opt == "5":
        break
    user_a = input("choose the first number ")
    user_b = input("choose the second number ")

    match user_opt:
        case "1":
            print(add(user_a,user_b))
        case "2":
            print(substract(user_a,user_b))
        case "3":
            print(add(user_a,user_b))
        case "4":
            print(add(user_a,user_b))
        case _:
            continue

print("Thanks for using!")