import csv

def create_employees():
    data = []
    with open('employees_data.csv', 'r', newline='') as csvfile:
        filedata = csv.reader(csvfile)
        for i in filedata:
            data.append(i)
    return data


def create_customers():
    data = []
    with open('customers_data.csv', 'r', newline='') as csvfile:
        filedata = csv.reader(csvfile)
        for i in filedata:
            data.append(i)
    return data


def create_orders():
    data_employees = create_employees()
    data_customers = create_customers()
    data = []
    with open('orders_data.csv', 'r', newline='') as csvfile:
        filedata = csv.reader(csvfile)
        for i in filedata:
            data.append(i)
    return data

# ty1 = create_employees()
# ty2 = create_customers()
# ty3 = create_orders()
# print(ty3)