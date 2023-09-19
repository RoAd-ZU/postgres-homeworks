import psycopg2
import os.path
from north_data.csv_reader import create_employees, create_customers, create_orders

"""Скрипт для заполнения данными таблиц в БД Postgres."""


def create_table():
    password = input('Введите свой пароль postgres\n')
    table1 = psycopg2.connect(host='localhost', database='north', user='postgres', password=password)
    data1 = create_employees()
    data2 = create_customers()
    data3 = create_orders()
    try:
        with table1:
            for i in data1:
                if i != data1[0]:
                    with table1.cursor() as curso:
                        curso.execute("INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)", (i))

    finally:
        table1.close()

    try:
        with table1:
            for i in data2:
                if i != data2[0]:
                    with table1.cursor() as curso:
                        curso.execute("INSERT INTO customers VALUES (%s, %s, %s)", (i))
    finally:
        table1.close()

    try:
        with table1:
            for i in data3:
                if i != data3[0]:
                    with table1.cursor() as curso:
                        curso.execute("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)", (i))
    finally:
        table1.close()


if __name__ == '__main__':
    create_table()
