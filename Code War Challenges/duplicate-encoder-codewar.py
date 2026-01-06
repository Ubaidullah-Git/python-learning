def duplicate_encode(word):
    word = word.lower()
    return "".join("(" if word.count(n) == 1 else ")" for n in word )

print(duplicate_encode("din"))
print(duplicate_encode("recede"))
print(duplicate_encode("Success"))
print(duplicate_encode("(( @"))
print(duplicate_encode("aA"))
