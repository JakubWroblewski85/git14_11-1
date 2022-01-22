'''wytłumaczenie getter i setter = właściwości
https://www.youtube.com/watch?v=qDDUTDMljvk'''

class Pracownik:
    # wszystko po dwukroptu należy do tej klasy
    # klasy pozwalają nam na przechowywanie zmiennych funkcji
    # funkcje w klasie to metoda
    stan_konta_pracownika = 0

    # przerabiamy funkcje na prawie zwykłą zmienną mówimy na nią -włąściwość
    @property
    def stan_konta(self):
        return self.stan_konta_pracownika

    # gettery i settery tworzymy tylko dla właściwośći (gettery mają wiekszy prioryttet)
    @stan_konta.getter
    def stan_konta(self):
        return 'Stan konta: ' + str(self.stan_konta_pracownika) + 'zł'

    # setter umożliwia nam przypisac nam wartość do naszej zmiennej (właściwości)
    @stan_konta.setter
    def stan_konta(self, value):
        self.stan_konta_pracownika += value

pracownik = Pracownik()
# wczesniej przed zmianą funkcji na właściwość wywoływaliśmy funkcje tak:
# print(pracownik.stan_konta())

# teraz po zmianie funkcji na właściwość wywołujemy ją prościej
print(pracownik.stan_konta)
print(pracownik.stan_konta_pracownika)

# funkcja zadziała bo mamy setter
pracownik.stan_konta = 50
print(pracownik.stan_konta)
pracownik.stan_konta = 100
print(pracownik.stan_konta)
pracownik.stan_konta = -150
print(pracownik.stan_konta)

