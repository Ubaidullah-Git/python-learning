def get_middle(s):
    if len(s)%2 == 0:
        n = int(len(s)/2)
        return s[n - 1] + s[n]
    elif len(s)%2 != 0:
        n = int(len(s)/2)
        return s[n]
    elif len(s) == 1:
        return s

print(get_middle("height"))
print(get_middle("H"))
print(get_middle("Aeroplane"))
