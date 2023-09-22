"""Файл для получения данных из файлов в north_data"""
import csv


def create_data(file):
    data = []
    with open(file, 'r', newline='') as csvfile:
        filedata = csv.reader(csvfile)
        for i in filedata:
            data.append(i)
    return data
