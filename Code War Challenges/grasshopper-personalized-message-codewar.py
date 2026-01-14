def greet(name, owner):
    return f"Hello {'boss' if name == owner else 'guest'}"

def greet1(name, owner):
    return 'Hello {}'.format('boss' if name == owner else 'guest')

def greet2(name, owner):
    return 'Hello boss' if name == owner else 'Hello guest'

print(greet1("Alice", "Alice"))
print(greet2("Bob", "Alice"))
print(greet("John", "John"))
print(greet1("Emma", "Liam"))
print(greet2("", ""))
