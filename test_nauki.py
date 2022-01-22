# konstruckaj klasy


    # funkcje klasy - method


    # służu do reprezentacji objektu, reprezentacja obieku jest wtedy jak chce wyprintować ten objekt.

    # tworze objekty
    # instancje klasy w klasie innej


# self moge używać teraz już w całej klasie :)


'''
cwiczenia z youtube
'''


# klasy nie wystarczy wypisać trzeba je jeszcze wywyłąć
class Pracownik:
    def __init__(self,imie, nazwisko, pensja):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pensja = pensja
        self.all_pensja = [self.pensja]

    def __repr__(self):
        return self.imie + ' ' + self.nazwisko

# moduł HR
class HR:
    def __init__(self):
        self.marcin_nowak = Pracownik("Marcin", "Nowak", 5000)
        self.joanna_kowalska = Pracownik("Joanna", "Kowalska", 5000)
        self.barbara_matysiak = Pracownik("Barbara", "Matysiak", 4000)
        self.pracownicy = [self.marcin_nowak, self.joanna_kowalska, self.barbara_matysiak]

    def wylicz_mies_pensje(self):
        suma = 0
        for pracownik in self.pracownicy:
            print('Pracownik plus jego pensja:   ', pracownik, pracownik.pensja)
            suma += pracownik.pensja
        print(suma)

    def dodaj_pracownika(self):
        self.pracownicy.append(new_pracownik)

    def wypisz_wszystkich_pracownikow(self):
        print(self.pracownicy)


new_pracownik = Pracownik('Kamil', 'Ślimak', 4500)
modul_hr = HR()
modul_hr.dodaj_pracownika()
modul_hr.wylicz_mies_pensje()
modul_hr.wypisz_wszystkich_pracownikow()





