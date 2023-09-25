import psycopg2
from pathlib import Path
from north_data.csv_reader import create_data

"""Скрипт для заполнения данными таблиц в БД Postgres."""

def create_table():
    password = input('Введите свой пароль postgres\n')
    table1 = psycopg2.connect(host='localhost', database='north', user='postgres', password=password)

    # file1 = Path('north_data', 'employees_data.csv')
    file1 = Path(__file__).parent.joinpath('north_data').joinpath('employees_data.csv')
    file2 = Path(__file__).parent.joinpath('north_data').joinpath('customers_data.csv')
    file3 = Path(__file__).parent.joinpath('north_data').joinpath('orders_data.csv')

    data1 = create_data(file1)
    data2 = create_data(file2)
    data3 = create_data(file3)

    try:
        with table1:
            for i in data1:
                if i != data1[0]:
                    with table1.cursor() as curso:
                        curso.execute("INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)", (i))

        with table1:
            for i in data2:
                if i != data2[0]:
                    with table1.cursor() as curso:
                        curso.execute("INSERT INTO customers VALUES (%s, %s, %s)", (i))

        with table1:
            for i in data3:
                if i != data3[0]:
                    with table1.cursor() as curso:
                        curso.execute("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)", (i))
    finally:
        table1.close()


if __name__ == '__main__':
    create_table()
