
print("Witaj w programie obliczanie BMI. Podawaj liczby naturalne i tylko liczby.\n")
wzrost = float(input("Proszę podaj swój wzrost w metrach np. (metr 82 cm = 1.82)\n"))
waga = float(input("Proszę podaj swoją wage w kg\n"))

def bmi(wzrost, waga):
    bmi_wynik = waga / (wzrost * wzrost)
    print("Twoje BMI to:\n", bmi_wynik)
    if bmi_wynik < 18.5:
        print("\nInterpretacja wyników:\n Niedowaga")
    elif bmi_wynik >= 18.5 and bmi_wynik < 24.99:
        print("\nInterpretacja wyników:\n Wartość prawidłowa GRATULACJE")
    elif bmi_wynik >= 24.99:
        print("\nInterpretacja wyników:\n -nadwaga (proponuje nie dojadać i zacząc coś ćwiczyć...")

bmi(wzrost, waga)
