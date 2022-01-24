import calculator

calc = calculator.Calculator()

result = calc.dodaj(4, 6)
print(result)
resul_extended = calc.add_extended(1, 2, 3, 98)
print(resul_extended)

calc.add_named(a=6, b=9)
