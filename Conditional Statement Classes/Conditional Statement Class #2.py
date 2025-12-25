import time

Time = time.strftime("%H:%M:%S")
print(Time)

Time_H = int(time.strftime("%H"))
print(Time_H)

Time_M = int(time.strftime("%M"))
print(Time_M)

Time_S = int(time.strftime("%S"))
print(Time_S)

if Time_H >= 5 and Time_H <= 11:
    print("Good Morning")
elif Time_H >= 12 and Time_H <= 16:
    print("Good Afternoon")
elif Time_H >= 17 and Time_H <= 18:
     print("Good Evening")
else:
    print("Good Night")
