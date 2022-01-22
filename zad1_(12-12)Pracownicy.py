class Pracownik:
    def __init__(self, imie, nazwisko, pensja):
        self.set_imie(imie)
        self.set_nazwisko(nazwisko)
        self.set_pensja(pensja)

    # przerobienie prawie na zwykłą zmienną -właściwość
    # @property
    # def get_imie(self):
    #     return self.imie

    # gettery i settery tworzymy tylko dla własciwości (property)
    # automatycznie jest wywoływana funckaj getter ma większy priorytet
    def get_imie(self):
        return self.imie

    def set_imie(self, imie):
        self.imie = imie

    def get_nazwisko(self):
        return self.nazwisko

    def set_nazwisko(self, nazwisko):
        self.nazwisko = nazwisko

    def get_pensja(self):
        return self.pensja

    def set_pensja(self, pensja):
        self.pensja = pensja


nowak = Pracownik("Marcin", "Nowak", 5000)
kowalska = Pracownik("Joanna", "Kowalska", 5000)
matysiak = Pracownik("Barbara", "Matysiak", 4000)

print('nowak imie: ', nowak.get_imie())
print('nowak nazwisko: ', nowak.get_nazwisko())
print('nowak pensja: ', nowak.get_pensja())
nowak.set_imie(' Zbyszek')
print('nowak imie: ', nowak.get_imie(), '\n')