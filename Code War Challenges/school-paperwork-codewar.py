def paperwork(n, m):
    if n < 0 or m < 0:
        return 0
    else:
        return m*n

print(paperwork(4,5))
print(paperwork(3,0))
print(paperwork(0,0))
print(paperwork(0,5))
print(paperwork(13,54))
