def nb_year(p0, percent, aug, p):
    year = 0
    rate = percent/100
    while(p0 < p):
        p0 += int(p0*rate) + aug
        year += 1
    return year

print(nb_year(1000, 2, 50, 1200))
print(nb_year(1500, 5, 100, 5000))
print(nb_year(1500000, 2.5, 10000, 2000000))
print(nb_year(500, 10, 50, 1000))
print(nb_year(2000, 0, 100, 2500))
