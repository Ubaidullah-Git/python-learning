def sum_array(arr):
    if not arr:
        return 0
    elif len(arr) == 1:
        return 0
    else:
        return sum(arr) - max(arr) - min(arr)

print(sum_array([]))
print(sum_array([5]))
print(sum_array([1, 2]))
print(sum_array([6, 2, 1, 8, 10]))
print(sum_array([1, 1, 11, 2, 3]))
print(sum_array([-6, -20, -1, -10]))
