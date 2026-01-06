def duplicate_count(text):
    duplicate_ch = ""
    text = text.lower()
    for s in text:
        if text.lower().count(s) > 1 and s not in duplicate_ch: duplicate_ch += s
    return len(duplicate_ch)

print(duplicate_count("aabBcde"))
print(duplicate_count("Indivisibility"))
print(duplicate_count("abcde"))
print(duplicate_count(""))
