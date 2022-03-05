class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def say_hello(self):
        return f'{self.first_name} {self.last_name}'


zbyszek = Student('Zbyszek', 'Nowak')
zbyszek.first_name = 'Heniek'

print('Obiekt', zbyszek)
print('First name', zbyszek.first_name)
print('Last name', zbyszek.last_name)

malgosia = Student('Małgorzata', 'Briegert')
print(malgosia.first_name, malgosia.last_name)

print(malgosia.say_hello())




