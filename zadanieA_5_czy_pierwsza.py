num = int(input("Wpisz liczbe: "))
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "to nie jest liczba pierwsza")
            break
    else:
        print(num, "to jest liczba pierwsza")
else:
    print(num, "to nie jest liczba pierwsza, musi być większa od 1")

