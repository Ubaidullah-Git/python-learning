# Strings are immutable

str_1 = 'Pakistan'

print("\n\n\nstr_1[1:9] = \"Lahore\"\n    ~~~~~^^^^^\nTypeError: 'str' object does not support item assignment\n\n\n")

# upper()
print(str_1.upper())

# lower()
print(str_1.lower())

str_2 = "@Lahore@"

# strip()
print(str_2.strip("@"))

# rstrip()
print(str_2.rstrip('@'))

# replace()
print(str_2.replace('@Lahore@',"Pakistan"))
print(str_1.replace("Pakistan",'Lahore'))

str_3 = "Lahore Karachi Peshawar Multan "

# split()
print(str_3.split( ))

str_4 = 'introduction to js'

# capitalize()
print(str_4.capitalize())

str_5 = 'What?'

# center()
print(str_5.center(20))
print('\n')
print(len(str_5.center(20)))
print('\n')
print(len(str_5))

# count()

print(str_2.count("@"))

# endswith()

print(str_2.endswith('@'))  #True because string starts with @
print(str_2.endswith('L'))  #False because string starts with @

print(str_3.endswith('ra',7,11))

# startswith()

print(str_2.startswith('@'))  #True because string ends with @
print(str_2.startswith('L'))  #False because string ends with @

print(str_3.startswith('Ka',7,11))

# find()

print(str_3.find("war"))
print(str_3.find("sar "))

# index()

# print(str_3.index('re s'))

print(str_3.index('re'))
print("\n\n\nprint(str_3.index('re s'))\n          ~~~~~~~~~~~^^^^^^^^\nValueError: substring not found\n\n\n")

# isalnum()

str_6 = "IsalNum123"

print(str_3.isalnum())
print(str_6.isalnum())

# isalpha()

str_7 = 'Isalpha'

print(str_6.isalpha())
print(str_7.isalpha())

# islower()

print(str_4.islower())
print(str_5.islower())

# isupper()

str_8 = "ISLAMABAD"

print(str_5.isupper())
print(str_8.isupper())

# isprintable()

str_9 = "Where is Lahore\n"

print(str_9.isprintable())
print(str_8.isprintable())

# isspace()

str_10 = "      "

print(str_10.isspace())
print(str_8.isspace())

# istitle()

str_11 = "University Of Central Punjab"

print(str_11.istitle())
print(str_8.istitle())

# title()

print(str_8.title())


# swapcase()

print(str_4.swapcase())
print(str_8.swapcase())
