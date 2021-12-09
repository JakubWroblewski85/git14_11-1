
oceny_str = input('Podaj oceny oddzielone pzrecinkiem')

# sprawdzam typ
print(type(oceny_str))
oceny_list = oceny_str.split(',')
print(oceny_list)

# wyswietl zawartosc listy
# element po elemencie

print('ilosc elementow w liscie', len(oceny_list))
ilosc_ocen = len(oceny_list)

suma = 0
for ocena in oceny_list:
    suma = suma + float(ocena)
    wynik = suma/ilosc_ocen
    print(wynik)

