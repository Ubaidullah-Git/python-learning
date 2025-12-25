x = 0
while (x <= 10):
    if (x == 7):
         x += 1 
         break
    print(x)
    x += 1 

print('Loop is Skipped')

print('\n')

x = 0
while (x <= 10):
    if (x == 7):
         x += 1
         print('Iteration is Skipped') 
         continue
    print(x)
    x += 1 

x = 0
while (x >= 0):
         print(x)
         x += 1