
ft = int(input("Najpierw podaj wysokość w ft (foot) i potem wcisnij klawisz 'ENTER'\n"))
cal = int(input("Teraz podaj wysokosć w cal (inch) i wcisnij 'ENTER'\n"))

ft_cm = (12 * 2.54)
cal_cm = (2.54)

def konwersja(ft, cal):
    calkowita_wysokosc_w_cm = 0

    if ft > 0:
        calkowita_wysokosc_w_cm += (ft_cm * ft)
    if cal > 0:
        calkowita_wysokosc_w_cm += (cal_cm * cal)
    print("Całkowita wysokość w centymetrach wynośi:")
    return calkowita_wysokosc_w_cm

print(konwersja(ft, cal))
