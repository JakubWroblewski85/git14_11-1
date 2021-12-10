
pojemnik = []
for liczba in range(2000,3000):
    if liczba %7 == 0 and liczba %5 != 0:
        pojemnik.append(liczba)
print(pojemnik)
