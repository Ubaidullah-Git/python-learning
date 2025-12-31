def sum_array(a):
    if not a:
        return 0
    return sum(a)

print(sum_array([]))
print(sum_array([1, 2, 3]))
print(sum_array([5]))
print(sum_array([-1, -2, -3]))
print(sum_array([1, -2, 3, -4]))
print(sum_array([1.5, 2.5, 3]))
print(sum_array([0, 0, 0]))
print(sum_array([100, 200, 300]))