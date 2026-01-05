def descending_order(num):
    if len(list(str(num))) > 1:
        lst = list(str(num))
        lst.sort(reverse=True)
        return int("".join(lst))
    else:
        return num

n1 = 7
n2 = 35784
n3 = 234738234520890
print(descending_order(n1))
print(descending_order(n2))
print(descending_order(n3))
