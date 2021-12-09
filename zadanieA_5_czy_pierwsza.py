
liczba = int(input("Podaj liczbę naturalną, sprawdzimy ją czy jest to liczba pierwsza...\n"))
print("Liczba pierwsza to taka liczba która da sie podzielić przez 2 inne liczby naturalne.\n")

if liczba %2 != 0:
    print(liczba %2 !=0)
    print("Liczba podana przez Ciebie", liczba, "jest liczbą pierwszą")
else:
    print(liczba %2 !=0)
    print("Liczba podana przez Ciebie", liczba, "nie jest liczbą pierwszą")