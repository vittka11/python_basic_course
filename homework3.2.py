number = [12, 3, 4, 10]
if len(number) > 1:
    last = number.pop()
    number.insert(0, last)
    print(number)

number = [12, 3, 4, 10, 8]
if len(number) > 1:
    last = number.pop()
    number.insert(0, last)
    print(number)

number = [1]
if len(number) > 1:
    last = number.pop()
    number.insert(0, last)
    print(number)

number = []
if len(number) > 1:
    last = number.pop()
    number.insert(0, last)
    print(number)
