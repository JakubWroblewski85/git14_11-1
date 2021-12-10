Kolory = ['czerwony', 'zielony', 'niebieski', 'czarny']

# print(Kolory[0])
# print(Kolory[-1])

ferst = []
the_last = []
def ferst_and_the_last(Kolory):
    ferst.append(Kolory[0])
    the_last.append(Kolory[-1])
    return "Pierwszy kolor z listy to:\n", ferst, "Zaś ostatni kolor z listy to:\n", the_last
    
print(ferst_and_the_last(Kolory))
