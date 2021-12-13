
# cala krotka definicja objektowa znaczy ze ja moge tworzyc wlasne klocki typy danych

# Tworzenie klasy
# klasa jest szablon
class Czlowiek:
    # cialo klasy
    gatunek = "homo sapiens"
    def __init__(self, imie, nazwisko):
        print("jeste gatunku", self.gatunek)
        print("Tworzę człowieka o imieniu", imie, nazwisko)
        self.imie = imie
        self.nazwisko = nazwisko
        # adam.imie = "Adam"
        # ewa.imie = "Ewa"

    def powiedz_hej(self):
        print("No hej. Jestem", self.imie)

adam = Czlowiek('Adam', 'Pierwszy') # self = adam
ewa = Czlowiek('Ewa', 'Pierwsza') # self = ewa
# print(dir(adam))
print(adam.imie)
print(ewa.imie)
adam.powiedz_hej()
ewa.powiedz_hej()


'''
print(dir(Czlowiek))
print(type(Czlowiek))
print(type(int))
'''

'''
# tworzę OBIEKT
# INSTANCJA klasy Człowiek
adam = Czlowiek()
ewa = Czlowiek()
print(type(adam))
print(adam.gatunek)
print(dir(adam))
print(ewa.gatunek)

adam.powiedz_hej()
ewa.powiedz_hej()

# to samo maja w dir
print(dir(Czlowiek))
print(dir(adam))
'''

