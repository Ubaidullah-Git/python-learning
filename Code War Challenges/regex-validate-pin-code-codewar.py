def validate_pin(pin):
    if len(pin) == 4 or len(pin) == 6:
        if pin.isdigit():
            return True
        else:
            return False
    else:
        return False

print(validate_pin("123"))
print(validate_pin("5436"))
print(validate_pin("12378"))
print(validate_pin("784677"))
print(validate_pin("7q84er"))