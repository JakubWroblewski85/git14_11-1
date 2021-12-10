
# założenia silni= liczby mogą być tylko naturalne, nie mogą być to liczby ujemne
# silnia 0! jest to 1

liczba = int(input("Podaj liczbę naturalną dodatnią a my zwrócimy wam jej silnie\n"))

try:
    if liczba < 19999 and liczba >= 0:
        silnia = 1
        for i in range(liczba):
            silnia = silnia * (i+1) 
        print(silnia)
    else:
        print("Za duża liczba lub za mała")
except:
    print("błędne dane")