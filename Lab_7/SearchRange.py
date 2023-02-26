import csv
from write import write_data

def search_range(val, start_range, end_range):
    with open('BankChurners.csv', 'r',) as fbank:
        reader = csv.DictReader(fbank)
        for row in reader:
            if float(start_range) <= float(row[val]) <= float(end_range):
                print(row)
                write_data(row)