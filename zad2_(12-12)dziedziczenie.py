class Pracownik:
    def __init__(self, imie, nazwisko, pensja_miesieczna):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pensja = pensja_miesieczna


# dziedziczenie po klasie Pracownik
class Informatyk(Pracownik):
    def programuj(self):
        return 'programuję...'


# dziedziczenie po klasie Pracownik
class Ksiegowy(Pracownik):
    def roczna_pensja(self):
        suma = 0
        suma += self.pensja * 12
        return suma

informatyk = Informatyk("Marcin", "Nowak", 5000)
# informatyk = Pracownik("Marcin", "Nowak", 5000)
print(informatyk.programuj())



# instancja klasy informaty z dziedziczenia klasy Pracownik
# nowak = Pracownik("Marcin", "Nowak", 5000)
#
# kowalska = Informatyk("Joanna", "Kowalska", 4000)
# kowalska = Ksiegowy("Joanna", "Kowalska", 4000)
