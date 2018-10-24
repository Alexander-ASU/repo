class Employee:
    def __init__(self, name='', surname='', age=-1):
        self.name = name
        self.surname = surname
        self.age = age

    def read_from_console(self):
        self.name = input('Enter name: ')
        self.surname = input('Enter surname: ')
        self.age = int(input('Enter age: '))
        return self

    def __str__(self):
        res = self.name + ' '
        res += self.surname + ' '
        res += str(self.age)
        return res
