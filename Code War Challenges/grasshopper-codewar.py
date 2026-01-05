def get_grade(s1, s2, s3):
    if (s1+s2+s3)/3 >= 90 and (s1+s2+s3)/3 <= 100: return 'A'
    elif (s1+s2+s3)/3 >= 80 and (s1+s2+s3)/3 < 90: return 'B'
    elif (s1+s2+s3)/3 >= 70 and (s1+s2+s3)/3 < 80: return 'C'
    elif (s1+s2+s3)/3 >= 60 and (s1+s2+s3)/3 < 70: return 'D'
    elif (s1+s2+s3)/3 >= 0 and (s1+s2+s3)/3 < 60: return 'F'

print(get_grade(95, 90, 93))
print(get_grade(85, 80, 88))
print(get_grade(75, 70, 72))
print(get_grade(65, 60, 62))
print(get_grade(40, 50, 55))
