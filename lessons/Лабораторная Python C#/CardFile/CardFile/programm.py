from company import Company
from employee import Employee
from boss import Boss

def main():
    print('1 - Add Employee')
    print('2 - Add Boss')
    print('3 - Print employees')
    print('4 - Remove employee by index')
    print('5 - Save company to file')
    print('6 - Read company to file')
    print('7 - Exit')

    company = Company()
    while True:
        command = input('Enter command: ')
        if command == '1':
            emp = Employee()
            company.add_employee(emp.read_from_console())
        elif command == '2':
            boss = Boss()
            company.add_employee(boss.read_from_console())
        elif command == '3':
            print(company)
        elif command == '4':
            index = int(input('Enter index: '))
            del company.employees[index]
        elif command == '5':
            fname = input('Enter file name: ')
            company.write_to_file(fname)
        elif command == '6':
            fname = input('Enter file name: ')
            company = Company.read_from_file(fname)
        elif command == '7':
            break
        else:
            print('Wrong command!')

if __name__ == '__main__':
    main()
    #company = Company()
    #for _ in range(1):
    #    company.add_employee(Employee().read_from_console())
    #    company.add_employee(Boss().read_from_console())
    
    #company = Company.read_from_file('company_dump')
    #print(company)
    #company.write_to_file('company_dump')
    #pass