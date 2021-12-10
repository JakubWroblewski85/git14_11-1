# aby odpalić w konsoli trzeba przejsc do powyższej lokalizacji i wpisać:
# python3 zadanieB_7_histogram_pionowy.py

def histogram( list ):

    for e in list:

        toPrint = ''
        while( e > 0 ):
            toPrint += '__'
            e -= 1
        print(toPrint)

histogram([1,1,1,2,3,7,7,16])