def descending_order(num):
    if len(list(str(num))) > 1:
        return int("".join(sorted(str(num),reverse=True)))
    else:
        return num

n1 = 7
n2 = 35784
n3 = 234738234520890
print(descending_order(n1))
print(descending_order(n2))
print(descending_order(n3))
