import pickle

class Company():
    def __init__(self):
        self.path = 'cgi-bin/st05/data'
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def read_from_file(self):
        self.employees = pickle.load(open(self.path, 'rb'))

    def write_to_file(self):
        pickle.dump(self.employees, open(self.path, 'wb'))

    def get_html_table(self):
        res = """
            <table style="border:1px solid black;">
                <tr>
                    <th>Имя</th>
                    <th>Фамилия</th>
                    <th>Возраст</th>
                    <th>Должность</th>
                    <th>Номер парковки</th>
                </tr>
              """
        for e in self.employees:
            res += e.get_html_tr()
        return res + "</table>"

    def __str__(self):
        res = ''
        for i, e in enumerate(self.employees):
            res += str(i) + ' - ' + e.__str__() + '\n'
        return res[:-1]