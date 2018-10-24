#from employee import Employee
#from boss import Boss
import pickle

class Company():
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    @staticmethod
    def read_from_file(path):
        #with open(path, 'r') as f:
        #    self.employees = []
        #    for line in f:
        #        attrs = line.split()
        #        attrs[2] = int(attrs[2])
        #        if len(attrs) == 3:
        #            self.employees.append(Employee(*attrs))
        #        else:
        #            attrs[4] = int(attrs[4])
        #            self.employees.append(Boss(*attrs))
        return pickle.load(open(path, 'rb'))

    def write_to_file(self, path):
        #with open(path, 'w') as f:
        #    for e in self.employees:
        #        f.write(e.__str__() + '\n')
        pickle.dump(self, open(path, 'wb'))

    def __str__(self):
        res = ''
        for i, e in enumerate(self.employees):
            res += str(i) + ' - ' + e.__str__() + '\n'
        return res[:-1]