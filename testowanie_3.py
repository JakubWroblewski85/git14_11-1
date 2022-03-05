from math import ceil


class InvalidSemester(Exception):
    pass


class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.semester = 1

    def say_hello(self):
        return f'{self.first_name} {self.last_name}'

    def go_higher(self):
        self.semester += 1

    def go_down(self):
        if self.semester <= 1:
            raise InvalidSemester('Nie możesz tego zrobić')
        self.semester -= 1

    # przez dodany dekorator dostajemy sie do funkcji jak do zwykłej zmiennej
    @property
    def year(self):
        return ceil(self.semester / 2)


try:
    staszek = Student('Staszek', 'Nowak')
    print(staszek.first_name)
    staszek.go_down()

except InvalidSemester as message:
    print(message)
