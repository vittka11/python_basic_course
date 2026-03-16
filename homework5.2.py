while True:
    a = float(input("Enter first number:"))
    b= float(input("Enter second number:"))
    op = input("Enter operation (+, -, *, /):")
    if op == "+":
        result = a + b
    elif op == "-":
        result = a - b
    elif op == "*":
        result = a * b
    elif op == "/":
        result = a / b
    else:
        print("Invalid operation")
        continue
    print("result:" , result)
    cont = input("Do you want to continue? (yes/y):")
    if cont in ("yes" , "y"):
        continue
    else:
        print(" Thank you for using this program")
        break
