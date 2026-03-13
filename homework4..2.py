numbers = (0, 2, 5, 4, 3, 6)
if len(numbers) == 0:
    result = 0
else:
    sum_even = 0
    for i in range(0, len(numbers),2):
        sum_even += numbers[i]
    result = sum_even * numbers[-1]
print(result)
