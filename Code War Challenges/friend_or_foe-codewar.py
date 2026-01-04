def friend(x):
    friend = []
    for name in x:
        if len(name) == 4:
            friend.append(name)
    return friend

l1 = ['Ahmad','Ali','Musa','Aoun','Daniyal',]
print(friend(l1))
