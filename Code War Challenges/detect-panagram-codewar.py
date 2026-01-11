def is_pangram(st):
    return len({s for s in st.lower() if s.isalpha()}) == 26

print(is_pangram("The quick brown fox jumps over the lazy dog"))
print(is_pangram("Sphinx of black quartz, judge my vow"))
print(is_pangram("Pack my box with five dozen liquor jugs")) 
print(is_pangram("Hello World"))
print(is_pangram("abcdefghijklmnopqrstuvwxyz"))
print(is_pangram("Missing some letters here"))
