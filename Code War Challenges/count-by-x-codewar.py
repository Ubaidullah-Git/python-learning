def count_by1(x, n):
    return [*range(x,x*n+1,x)]

def count_by2(x, n):
    return list(range(x,x*n+1,x))

def count_by3(x, n):
    return [x*(i+1) for i in range(n)]

def count_by(x, n):
    lst = []
    for i in range(n):
        lst.append(x*(i+1))
    return lst

print(count_by(2,6))
print(count_by1(23,64))
print(count_by2(14,45))
print(count_by3(9,17))
