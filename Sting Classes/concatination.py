def solution(string):
    reverse = ''
    range = len(string)

    while(range > 0):
        reverse = reverse + string[range - 1]
        range = range - 1
    return reverse

result = solution('world')
print(result)