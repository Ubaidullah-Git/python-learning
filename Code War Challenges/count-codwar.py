def count_sheeps(sheep1):
    return sheep1.count(True)

sheep_array = [True, True, False, True, False, True]
print(count_sheeps(sheep_array))

def count_sheeps(sheep):
    count = 0
    for s in sheep:
        if s is True:
            count += 1  
    return count


sheep_array = [True, True, True, False, False, True, False, True]
print(count_sheeps(sheep_array))

