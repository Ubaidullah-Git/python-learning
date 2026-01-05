def unique_in_order(sequence):
    lst = []
    for x in sequence:
        if x not in lst or x != lst[-1]:
            lst.append(x)
    return lst

print(unique_in_order('AAAABBBCCDAABBB'))
print(unique_in_order('ABBCcAD'))
print(unique_in_order([1, 2, 2, 3, 3]))
print(unique_in_order((1, 2, 2, 3, 3)))
