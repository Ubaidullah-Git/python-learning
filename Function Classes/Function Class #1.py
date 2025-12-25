def percentage(subject):
    obt_marks = float(input(f"Enter Your Obtained Marks in {subject}:"))
    total_marks = int(input("Enter Total Marks: "))
    percentage = (obt_marks/total_marks)*100
    print(f"Your Percentage in {subject} is",percentage)
    print("\n")


percentage("URDU")
percentage("ENGLISH")
percentage("PAK-STD")
percentage("ISLAMIAT")
percentage("TARJAMA-TUL-QURAN")
percentage("MATHEMATICS")
percentage("PHYSICS")
percentage("COMPUTER")


