def basic_op(operator, value1, value2):
    if operator == '+':
        return value1 + value2
    elif operator == '-':
        return value1 - value2
    elif operator == '*':
        return value1 * value2
    elif operator == '/':
        return value1 / value2
    else:
        return "Invalid Operator."
    
print(basic_op('+', 5, 3))
print(basic_op('-', 10, 4))
print(basic_op('*', 6, 7))
print(basic_op('/', 20, 4))
print(basic_op('/', 7, 2))
print(basic_op('%', 10, 3))
