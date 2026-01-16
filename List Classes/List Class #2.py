# use of append()

l = [2,4,5,6,7]
print(l)
l.append(9)
print(l)

# use of sort()

lst = [3,5,2,7,1,4,6,7,43,65,66,45,33,56,34,44,32,24,36,33,21,25,14,16]
print(lst)
lst.sort()
print(lst)
lst.sort(reverse=True)
print(lst)

# use of reverse()

ls = [3,5,5,6,3,6,2,77,54,77,75,24,43,23,21,16,16,14,134,46,35,67,34]
print(ls)
ls.reverse()
print(ls)

# use of index()

print(ls.index(77))
print(ls.index(21))
print(lst.index(36))
print(ls.index(5))

# use of count()

print(ls.count(77))
print(ls.count(21))
print(lst.count(36))
print(ls.count(5))



