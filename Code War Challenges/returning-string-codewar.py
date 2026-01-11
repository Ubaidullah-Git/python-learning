def greet1(name):
    return "Hello, "+name+" how are you doing today?"

def greet2(name):
    return f"Hello, {name} how are you doing today?"

def greet3(name):
    return "Hello, {} how are you doing today?".format(name)

print(greet1("Alice"))
print(greet2("Bob"))
print(greet3("Zara"))
