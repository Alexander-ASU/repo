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

    def get_html_tr(self):
        return """
               <tr>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%d</td>
                    <td>—</td>
                    <td>—</td>
               </tr>
               """ % (self.name, self.surname, self.age)

    def __str__(self):
        res = self.name + ' '
        res += self.surname + ' '
        res += str(self.age)
        return res
