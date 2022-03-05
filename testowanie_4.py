# lista = ["ala","ma","kota"]
# print(lista[0], lista[1], lista[2])
# print(*lista)
# print(lista)

def funkcja(a=None, b=None):
    print("a =", a)
    print("b =",b)

funkcja(1,2)
# a = 1
# b = 2
funkcja(*(1,2))
# a = 1
# b = 2
funkcja((1,2))
# a = (1, 2)
# b = None