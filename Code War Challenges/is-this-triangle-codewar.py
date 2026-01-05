def is_triangle(a, b, c):
    return True if a+b>c and a+c>b and b+c>a else False

print(is_triangle(3, 4, 5))
print(is_triangle(1, 2, 3))
print(is_triangle(5, 5, 5))
print(is_triangle(0, 2, 2))
