import csv
from write import write_data

def search_first_letter(val,letter):
    with open('BankChurners.csv', 'r',) as fbank:
        reader = csv.DictReader(fbank)
        for row in reader:
            if row[val][0]==letter:
                print(row)
                write_data(row)