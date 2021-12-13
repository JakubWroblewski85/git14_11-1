# założenia silni= liczby mogą być tylko naturalne, nie mogą być to liczby ujemne
# silnia 0! jest to 1
'''
# Definicja funkcji
def funkcja():
    # Zestaw poleceń
    print('1 polecenie')
    print('2 polecenie')

def sokowirowka(owoc):
    print("Robie sok z ", owoc)
    return "sok z " + owoc

# Wywołanie funkcji
sok = sokowirowka('jablko')

print(sok)
'''

# liczba = int(input("Podaj liczbę naturalną dodatnią a my zwrócimy wam jej silnie"))
# def silnia_iterative(liczba):
#     silnia = 1
#     for i in range(liczba):
#         silnia = silnia * (i+1)
#     return silnia

# print(silnia_iterative(liczba))
# silnia_iterative(liczba) dlaczego w tym przypadku nie wypisuje mi wyniku ?

liczba = int(input("Podaj liczbę naturalną dodatnią a my zwrócimy wam jej silnie"))
def silnia_recursive(liczba):
    if liczba <= 1:
        # if liczba in (0,1)
        return 1
    else:
        return liczba * silnia_recursive(liczba - 1)

print(silnia_recursive(liczba))
# funkcja recurencyjna to funkcja która wywołuje samą siebie wewnątrz swojego ciała.


