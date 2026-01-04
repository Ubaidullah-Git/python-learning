def binary_array_to_number(arr):
    s = "".join(str(digit) for digit in arr)
    d = int(s,2)
    return d

arr = [1,0,1,1,0,1,1,1,0,1,0,0,1,0]
print(binary_array_to_number(arr))
