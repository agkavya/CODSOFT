cont = True
while cont:
    print("1: Addition\n2:Subtraction\n3:Multiplication\n4:Division\n5:Remainder")
    choice = int(input("Select the operation (1-5)"))
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    if choice == 1:
        print(num1, "+", num2, "=", num1+num2)
    elif choice == 2:
        print(num1, "-", num2, "=", num1+num2)
    elif choice == 3:
        print(num1, "*", num2, "=", num1*num2)
    elif choice == 4:
        print(num1, "/", num2, "=", num1/num2)
    elif choice == 5:
        print(num1, "%", num2, "=", num1+num2)
    else:
        print("Enter the valid input!")
    ask = input("Do you want to continue? (y/n)")
    if ask == "y":
        cont = True
    else:
        cont = False
        exit()

