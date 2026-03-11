number = [1, 2, 3, 4, 5, 6]
if len(number) == 0:
    result = [[], []]
print(number, "=>" result)
elif len(number) % 2 == 0:
    middle = len(number) // 2
    result = [number[:middle], number[middle:]]

else:
    middle = len(number) // 2 + 1
    result = [number[:middle], number[middle:]]
print(result)
print(number, "=>", result)
