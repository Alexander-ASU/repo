from .company import Company
from .employee import Employee
from .boss import Boss

def main(q, self_url):
    c = Company()
    c.add_employee(Employee('john', 'stev', 25))
    c.add_employee(Boss('Pepe', 'Moki', 42, 'Chief', 66))
    print(
        """
        <!DOCTYPE html>
        <html lang="ru">
        <head>
            <title>Alex Gurin</title>
            <meta charset='utf-8'>
        </head>
        <body>
            %s
        </body>
        """ 
        % c.get_html_table()
    )
