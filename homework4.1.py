numbers = [0, 1, 0, 12, 3]
for i in numbers:
   if i == 0:
      numbers.remove(i)
      numbers.append(0)
print(numbers)

numbers = [0]
for i in numbers:
   if i == 0:
      numbers.remove(0)
      numbers.append(0)
print(numbers)

numbers = [1, 0, 13, 0, 0, 0, 5]
for i in numbers:
   if i == 0:
      numbers.remove(i)
      numbers.append(0)
print(numbers)

numbers = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
for i in numbers:
   if i == 0:
      numbers.remove(i)
      numbers.append(0)
print(numbers)