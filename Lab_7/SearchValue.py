import csv
from write import write_data

def search_value(val,var):
    with open('BankChurners.csv', 'r',) as fbank:
        reader = csv.DictReader(fbank)
        for row in reader:
            if row[val]==var:
                print(row)
                write_data(row)