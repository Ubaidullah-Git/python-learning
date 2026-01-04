def high_and_low(number):
    num = [int (x) for x in number.split()]
    highest = max(num)
    lowest = min(num)
    return str(highest) + " " + str(lowest)

print(high_and_low("3 45 -454 302 -32 -23 42"))
