from .employee import Employee

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

    def get_html_tr(self):
        return """
               <tr>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%d</td>
                    <td>%s</td>
                    <td>%d</td>
               </tr>
               """ % (self.name, self.surname, self.age,
                      self.position, self.parking_no)

    def __str__(self):
        res = super().__str__()
        res += ' ' + self.position + ' '
        res += str(self.parking_no)
        return res