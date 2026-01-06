def sum_two_smallest_numbers(num):
    return sum(sorted(num)[0:2])

print(sum_two_smallest_numbers([19, 5, 42, 2, 77]))
print(sum_two_smallest_numbers([10, 3, 8, 1]))
print(sum_two_smallest_numbers([5, 5, 5, 5]))
print(sum_two_smallest_numbers([2, 9, 1, 6]))
