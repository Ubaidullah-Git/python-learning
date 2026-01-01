def string_to_array(s):
    if s == '':
        return ['']
    return s.split()

print(string_to_array("Hello world"))
print(string_to_array("   Leading spaces"))
print(string_to_array("Split\tthis\nstring"))
print(string_to_array(""))