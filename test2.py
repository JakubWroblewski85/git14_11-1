# PROGRAM KSIĘGOWY
# MAMY FIRMĘ ZŁOŻONĄ Z 3 UŻYTKOWNIKÓW

imie_pracownik1 = "Marcin"
imie_pracownik2 = "Joanna"
imie_pracownik3 = "Barbara"

nazwisko_pracownika1 = "Nowak"
nazwisko_pracownika2 = "Kowalska"
nazwisko_pracownika3 = "Matysiak"


class Pracownik:
    def __init__(self, imie, nazwisko, pensja_startowa):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pensja = pensja_startowa

    # repr służy do reprezentacji objektu,
    # eprezentacja obieku jest wtedy jak chcemy wyprintować ten objekt.
    def __repr__(self):
        return self.imie + ' ' + self.nazwisko


class HR:
    def __init__(self):
        # tworze objekty
        # instancje klasy HR w klasie Pracownik
        self.marcin_nowak = Pracownik("Marcin", "Nowak", 5000)
        self.joanna_kowalska = Pracownik("Joanna", "Kowalska", 5000)
        self.barbara_matysiak = Pracownik("Barbara", "Matysiak", 4000)

        self.pracownicy = [self.marcin_nowak, self.joanna_kowalska, self.barbara_matysiak]

    # dodaje metodę -(czyli funkcje do funkcji wewnatrz klasy)
    def wylicz_miesieczne_wydatki(self):
        wydatki = 0
        for pracownik in self.pracownicy:
            wydatki += pracownik.pensja
        return wydatki

    # dodaje metodę -(czyli funkcje) do funkcji wewnatrz klasy
    def dodaj_pracownika(self, pracownik):
        # print(type(pracownik))
        # print(self.pracownicy)
        # print(type(self.pracownicy))
        self.pracownicy.append(pracownik)

    # dodaje metodę -(czyli funkcje) do funkcji wewnatrz klasy
    def wyswietl_wszystkich_pracownikow(self):
        print(self.pracownicy)


modul_hr = HR()
testowy_pracownik = Pracownik("Test", "Testowy", 1000)
# modul_hr.wyswietl_wszystkich_pracownikow()
# modul_hr.dodaj_pracownika(testowy_pracownik)
modul_hr.wyswietl_wszystkich_pracownikow()
<<<<<<< HEAD
modul_hr.dodaj_pracownika(testowy_pracownik)
zmienna = modul_hr.wyswietl_wszystkich_pracownikow()
print(zmienna)
=======
print(modul_hr.wylicz_miesieczne_wydatki())
>>>>>>> b2ffadeb3f3be3a68aa469060a3aed0c5eade306

