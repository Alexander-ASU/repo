from employee import Employee

class Boss(Employee):
    def __init__(self, name='', surname='', age=-1,
                 position='', parking_no=-1):
        self.name = name
        self.surname = surname
        self.age = age
        self.position = position
        self.parking_no = parking_no

    def read_from_console(self):
        super().read_from_console()
        self.position = input('Enter positon: ')
        self.parking_no = int(input('Enter parking number: '))
        return self

    def __str__(self):
        res = super().__str__()
        res += ' ' + self.position + ' '
        res += str(self.parking_no)
        return res