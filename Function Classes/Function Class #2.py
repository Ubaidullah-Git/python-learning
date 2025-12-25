def avg(*num):
    sum = 0
    for i in num:
        sum = sum + i
    print('Average is:', sum/len(num))

avg(3,4,6,2,7,45,43,21,56,89,133,23)

print('\n')

def avg(*num):
    sum = 0
    for i in num:
        sum = sum + i
    return sum/len(num)

a = avg(3,4,6,2,7,45,43,21,56,89)
print("Average is:", a)

