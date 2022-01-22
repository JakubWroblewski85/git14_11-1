import modul

class FirstClass:
    def __new
    def __init__(self, value):
        # KONSTRUKTOR
        # iniciuje dane do tej daty
        self._data = value

    def set_data(self, value):
        self._data = value

    def display(self):
        print(self._data)


x = FirstClass('alicja')
y = FirstClass()

# x.set_data('Król')
x.display()

