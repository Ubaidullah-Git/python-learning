def fake_bin(x):
    return "".join("0" if int(n) < 5 else "1" for n in x)

print(fake_bin("45385593107843568"))
print(fake_bin("1234"))
print(fake_bin("56789"))
print(fake_bin("0"))
print(fake_bin("9081726354"))
