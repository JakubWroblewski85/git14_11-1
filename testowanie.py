# PROGRAM KSIĘGOWY
# MAMY FIRMĘ ZŁOŻONĄ Z 3 UŻYTKOWNIKÓW
imie_pracownik1 = "Marcin"
imie_pracownik2 = "Joanna"
imie_pracownik3 = "Barbara"

nazwisko_pracownika1 = "Nowak"
nazwisko_pracownika2 = "Kowalska"
nazwisko_pracownika3 = "Matysiak"

class Pracownik:
    def __init__(self, imie, nazwisko, pensja):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pensja = pensja

    def __repr__(self):
        return self.imie + ' ' + self.nazwisko


class HR:
    def __init__(self):
        self.marcin = Pracownik('Marcin', 'Nowak', 5000)
        self.barbara = Pracownik('Barbara', 'Matysiak', 4000)
        self.andrzej = Pracownik('Andrzej', 'Kwiatkowski', 5500)
        self.pracownicy = [self.marcin, self.barbara, self.andrzej]

    def wylicz_miesieczna_wydatki(self):
        wydatki = 0
        for pracownik in self.pracownicy:
            wydatki += pracownik.pensja
        return wydatki

    def dodaj_pracownika(self, pracownik):
        print(self.pracownicy)
        self.pracownicy.append(pracownik)
        print(self.pracownicy)

    def wszyscy_pracownicy(self):
        print('\nImiona wszystkich pracowników:')
        for pracownik in self.pracownicy:
            print(pracownik.imie)


modul_hr = HR()
zbyszek = Pracownik('Marcin', 'Nowak', 4500)
modul_hr.dodaj_pracownika(zbyszek)
print('Miesięczne wydatki na pensje pracowników:', modul_hr.wylicz_miesieczna_wydatki(), 'zł')
modul_hr.wszyscy_pracownicy()