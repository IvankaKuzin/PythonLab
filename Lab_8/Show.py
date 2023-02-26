import csv
from WriteSR import writeSR

def show():
    with open('BankChurners.csv', 'r',) as fbank:
        reader = csv.DictReader(fbank)
        for row in reader:
            print(row)
            writeSR(row)