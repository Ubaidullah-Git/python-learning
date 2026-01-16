def sort_array(arr):
    odd = iter(sorted(x for x in arr if x % 2 != 0))
    for i, n in enumerate(arr):
        if n % 2 != 0:
            arr[i] = next(odd)
    return arr

print(sort_array([5, 3, 2, 8, 1, 4]))
print(sort_array([7, 1]))
print(sort_array([2, 4, 6, 8]))
print(sort_array([9, 8, 7, 6, 5]))
print(sort_array([1, 11, 2, 3, 5]))

