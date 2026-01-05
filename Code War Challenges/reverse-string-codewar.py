def solution(string):
    return ' '.join(word[::-1] for word in string.split(' '))


result = solution('hello world')
print(result)