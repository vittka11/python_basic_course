number = int(input("Enter a number: "))
print("Square:", number ** 2)

a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("enter third number:"))
average = (a+b+c) / 3
print ("The average is", average)

minutes = int(input("Enter minutes:"))
hours = minutes // 60
remaining_minutes = minutes % 60
print("Hours:",hours)
print("Minutes:", remaining_minutes)

price = float(input("Enter price:"))
discount = float(input("Enter discount(%):"))
final_price = price - (price * discount / 100)
(print("Price after discount:", final_price))

number = int(input("Enter a number:"))
last_digit = number % 10
print("Last_digit:", last_digit)

length = float(input("Enter length:"))
width = float (input("Enter width:"))
perimeter = 2 * (length + width)
print("Perimeter:", perimeter)

number= input("Enter number:")
for digit in number:
    print(digit)







