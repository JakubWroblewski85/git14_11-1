a = 5
#
# def funkcja():
#     a = 12
#     b = 6
#     print("wartość a rowna się", a)
#     print("wartość a rowna się", b)
#
# funkcja()

'''
lista = [1,2,3]
krotka = (1,2,3)

słowniki:

slownik = {'jeden': 1, 'dwa': 2}
slownik2 = {'el1': [1,2,3]}
slownik2 = {(1,2,3): 'el1'}
print(slownik2[(1,2,3)])
'''
 
 
# tworzenie slownika
# klucz wartosc
en_to_es = {'cat' : 'gato', 'dog' : 'perro'}
# pobranie elementu ze slownika
print(en_to_es['cat'])
# dodanie nieistniejącego elementu (nadpisanie innej wartosci w kluczu)
en_to_es['mouse'] = 'el rato'
en_to_es['mouse'] = 'efdgd'

print(en_to_es['mouse'])
print(type(en_to_es))

# wyswietl wartosci
print((en_to_es.values()))
# wyswietl klucze
print((en_to_es.keys()))
print(type(en_to_es))

# bezpieczne odszukiwanie wartosci
# nie rzuci wyjątku  gdy go nie ma
print(en_to_es.get('mężczyzna'))
print(type(en_to_es.get('mężczyzna')))
print(en_to_es.get('mouse'))

# wyswietl elementy
print(en_to_es.items())

for key in en_to_es:
    print(key)


print("Itemy", en_to_es.items())
for item in en_to_es.items():
    print("element", item, "type", type(item))

# iterowanie po parach klucz : wartość
for key, value in en_to_es.items():
    print(key, "->", value)

# obietky bool
print('cat' in en_to_es)
print(type('cat' in en_to_es))
print('cat' not in en_to_es)

#
print("klucz", '->',key)
print(en_to_es)
print(en_to_es[key])
print("ile jest elementó w slowniku?", len(en_to_es[key]))



