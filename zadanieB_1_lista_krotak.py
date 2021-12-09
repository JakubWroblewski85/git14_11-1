
# liczby = input("Podaj liczby naturalne poprzedzając je\n")
# print(type(liczby))

liczby_user = 34,60,55,33,12,98
# print(type(liczby2))
liczby_list = list(liczby_user)
print(type(liczby_list))
print(liczby_list)

i = []
for liczba in liczby_list:
    i.append(liczba)
    print(type(i))
    i = liczby_list.insert(8,i)
# print(liczby_list)