mix = [True,33,32.3,"data",3+4j]
print(mix)
print(type(mix[-1]))


marks = [32,34,44,24,13,44,65,21,75,23,53,23,65,66,68,39,46,57,24,29,46,45,54]
print(marks)
print(len(marks))
print(marks[3])
print(marks[-2])
print(marks[:])
print(marks[1:-1])
print(marks[1:8])
print(marks[1:7:2])
print(marks[1:15:3])
print(marks[::-1])
print(marks[23:0:-1])


# Check wheather an item is present in the list 

if 0 in mix:
    print('Yes.')
else:
    print('No')

if 'datA' in ['Data','DATA','data']:
    print('Yes')
else:
    print('No')

# Making new list from existing list using List Comprehension Method

names = ['Ali','Ahmad','Akram','Junaid','Awais','Maryam','Sara','Ayesha','Daniyal','Anam','Farhan','Sana']
names_A = [a for a in names if a[0] == 'A']
print(names)
print(names_A)

