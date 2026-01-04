def count_positives_sum_negatives(arr):
    c = 0
    s = 0
    if not arr:
        return []
    for n in arr:
        if n > 0:
            c += 1
    for n in arr:
        if n < 0:
            s += n
    return [c,s]

arr1 = []
arr2 = [1,243,-33,32,-343,1123,13,34,11,78,-68,-5]
print(count_positives_sum_negatives(arr1))
print(count_positives_sum_negatives(arr2))
