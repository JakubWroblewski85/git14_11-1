# changed to rectagular pizza2.

pizza1_price = float(input('Cena pizzy 1: '))
pizza1_a = float(input('Bok krótszy pizza1:'))
pizza1_b = float(input('Bok dłuższy pizza1:'))
pizza2_price = float(input('Cena pizzy 2: '))
pizza2_a = float(input('Bok krótszy pizza2:'))
pizza2_b = float(input('Bok dłuższy pizza2:'))

pole1 = pizza1_a * pizza2_b * 2
pole2 = pizza2_a * pizza2_b

a = pizza1_price/pole1
b = pizza2_price/pole2*pole2

if a < b:
    print('Pizza 1 opłaca się bardziej')
elif a == b:
    print('Obie są równe')
else:
    print('Pizza 2 opłaca się bardziej')



