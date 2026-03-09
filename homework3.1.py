a = float(input("Enter the first number:"))
b = float(input("Enter the second number:"))
d = input("Enter the operation(+, -, *, /):")
if d == "+":
    print(a + b)
elif d == "-":
    print(a - b)
elif d == "*":
    print(a * b)
elif d == "/":
    if b != 0:
     print(a / b)
else:
    print("Cannot devide by zero")


