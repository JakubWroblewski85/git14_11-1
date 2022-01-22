# tworzenie klasy
# klasa jest szablonem
class Czlowiek:
    gatunek = 'homo sapiens'

    # self = się - siebie
    def __init__(self, imie, nazwisko):
        print('tworze czlowieka o imieniu', imie, nazwisko)
        self.imie = imie    # adam.imie = 'Adam'
        self.nazwa = nazwisko

    # dodaje metodę -(czyli funkcje) do funkcji wewnatrz klasy
    def powiedz_hej(self):
        print('Hej')


# tworze objekt
# instancje klasy czlowiek
adam = Czlowiek('Adam', 'Wąglik')   # self = adam, odnosi sie do konkretnego obiektu
ewa = Czlowiek('Ewa', 'Pierworodna')   # self = ewa
good = Czlowiek('Bóg', 'Wszechmogący')


# print(type(adam))
# print(adam.gatunek)
# adam.powiedz_hej()
# ewa.powiedz_hej()
# print('Tworzę czlowieka o imieniu', '\n', adam.imie, adam.nazwa)

