import csv
from WriteSR import writeSR

def range(val, start_range, end_range):
    with open('BankChurners.csv', 'r',) as fbank:
        reader = csv.DictReader(fbank)
        for row in reader:
            if float(start_range) <= float(row[val]) <= float(end_range):
                print(row)
                writeSR(row)