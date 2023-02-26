import csv
from Write import write_data
from tabulate import tabulate

def sort(val,reg):
    with open('BankChurners.csv', 'r', ) as fbank:
        reader = csv.DictReader(fbank)
        if reg=='спадання':
            sortedlist = sorted(reader, reverse=True, key=lambda row: (row[val]))
        if reg == 'зростання':
            sortedlist = sorted(reader, key=lambda row: (row[val]))
        write_data(sortedlist)
        print(tabulate(sortedlist),end='\n')

