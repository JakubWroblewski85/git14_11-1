# aby odpalić w konsoli trzeba przejsc do powyższej lokalizacji i wpisać:
# python3 zadanieB_7_histogram_poziomy.py

def histogram( list ):
    if all(n <= 0 for n in list):
        return
    else:
        _list = [
            (lambda x: x -1)(n) for n in list
        ]
        histogram(_list)

        toPrint = ''
        for n in list:
            if n > 0:
                toPrint += '| '
            else:
                toPrint += '  '
    print(toPrint)

histogram([0,1,1,1,2,3,7,7,14])