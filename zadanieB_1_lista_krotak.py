liczby = input("Podaj liczby naturalne odzielone przecinkami\n")

# sprawdzam typ
print(type(liczby))

liczby_list = liczby.split(',')
print(liczby_list)
print(tuple(liczby_list))
