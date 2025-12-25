num = int(input("Enter a positive number:"))

if (num % 2 == 0):
    print("This is even.")
else:
    print("This is odd.")

print("\n\n")

Percentage = float(input("Enter your Percentage: "))

if(Percentage >= 85.0):
    print("You got Grade A+")
elif(Percentage >= 80.0):
    print("You got Grade A")
elif(Percentage >= 70.0):
    print("You got Grade B+")
elif(Percentage >= 60.0):
    print("You got Grade B")
elif(Percentage >= 50.0):
    print("You got Grade C")
elif(Percentage >= 40.0):
    print("You got Grade D")
elif(Percentage >= 33.0):
    print("You got Grade E")
else:
    print('You got Grade F')

print("\n\n")

n1 = int(input("Enter First number: "))
n2 = int(input("Enter Second number: "))
n3 = int(input("Enter Third number: "))

if(n1 > n2):
    if(n1 > n3):
        print("The Biggest number is",n1)
elif(n2 > n3):
    print("The Biggest number is",n2)
else:
    print("The Biggest number is",n3)

