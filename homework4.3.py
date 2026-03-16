import random

n = random.randint(3, 10)
numbers = []
for i in range(n):
    numbers.append(random.randint(1, 10))
print("original list:", numbers)

new_list = [numbers[0], numbers[2], numbers[-2]]
print("New_list:", new_list)