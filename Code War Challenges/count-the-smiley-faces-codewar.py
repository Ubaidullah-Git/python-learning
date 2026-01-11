def count_smileys(arr):
    return sum((len(f) == 2 and f[0] in ';:' and f[1] in ')D') or
               (len(f) == 3 and f[0] in ';:' and f[1] in '-~' and f[2] in ')D')
               for f in arr)

print(count_smileys([':)', ';(', ';}', ':-D']))
print(count_smileys([';D', ':-(', ':-)', ';~)']))
print(count_smileys([';]', ':[', ';*', ':$', ';-D']))
print(count_smileys([]))
print(count_smileys([':)', ':D', ';-D', ';~)', ':-)']))
