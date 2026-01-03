def is_isogram(s):
    return len(set(s.upper())) == len(s.upper())

print(is_isogram("dewuidgiqudqw"))
print(is_isogram("degiquw"))
