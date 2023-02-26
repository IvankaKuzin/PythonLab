import csv
from Write import write_data
from tabulate import tabulate

def sort2(val1,val2,reg):
    with open('BankChurners.csv', 'r', ) as fbank:
        reader = csv.DictReader(fbank)
        if reg=='спадання':
            sortedlist = sorted(reader, reverse=True, key=lambda row: (row[val1],row[val2]))
        if reg == 'зростання':
            sortedlist = sorted(reader, key=lambda row: (row[val1], row[val2]))
        print("%s\n" % line for line in sortedlist)
        write_data(sortedlist)
        print(tabulate(sortedlist), end='\n')
