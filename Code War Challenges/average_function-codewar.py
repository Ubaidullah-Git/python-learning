def find_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

print(find_average([1, 2, 3, 4]))
print(find_average([10]))
print(find_average([]))
print(find_average([-2, -4, -6]))
print(find_average([1, -1, 3, -3]))