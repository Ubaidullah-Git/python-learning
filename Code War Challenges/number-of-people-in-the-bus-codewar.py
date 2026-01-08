def number(bus_stops): 
    return sum(n[0] - n[1] for n in bus_stops)

print(number([[10, 0], [3, 5], [2, 5]]))
print(number([[3, 0], [9, 1], [4, 10], [12, 2]]))
print(number([[5, 0], [2, 2], [1, 1]]))
print(number([[8, 0], [0, 3], [4, 1]]))
