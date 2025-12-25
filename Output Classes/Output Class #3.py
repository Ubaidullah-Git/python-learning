#variables and data types

'''
     variable = +ve/-ve non-decimal/decimal point value or complex value
     variable = 'chracter/string' or "chracter/string"
     variable = boolean value (True/ false)
'''
laptops = 5
these = 'laptops'
what = True
print(these,"are",laptops)
print('this is',what)


Complex_1 = complex(2,6)
Complex_2 = complex(-6,3)
Complex_3= complex(5,-2)
Complex_4 = complex(-3,-4)
Non_Decimal_positive =  663
Non_Decimal_negative =  -98
Decimal_positive =  542.452
Decimal_negative =  -343.34

print('The type of Complex_1 is:',type(Complex_1))
print('The type of Complex_2 is:',type(Complex_2))
print('The type of Complex_3 is:',type(Complex_3))
print('The type of Complex_4 is:',type(Complex_4))
print('The type of Non_Decimal_positive is:',type(Non_Decimal_positive))
print('The type of Non_Decimal_negative is:',type(Non_Decimal_negative))
print('The type of Decimal_positive is:',type(Non_Decimal_positive))
print('The type of Decimal_negative is:',type(Decimal_negative))

#calculation between assigned variables

a=56
b=49.3
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(int(a%b))