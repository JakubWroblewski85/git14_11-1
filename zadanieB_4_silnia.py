
liczba_user = int(input("Podaj liczbe naturalną np.8 my wyliczymy z niej silnie...\n"))

def silnia(liczba_user):
    if liczba_user <= 1:
        return 1
    else:
        return liczba_user * silnia(liczba_user -1)

print(silnia(liczba_user))
