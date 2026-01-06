def xo(s):
    return s.lower().count("x") == s.lower().count("o")

print(xo("xo"))
print(xo("xxOo"))
print(xo("xxxm"))
print(xo("Oo"))
print(xo("xXoO"))
print(xo("abc"))
