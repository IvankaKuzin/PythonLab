import csv
from write import write_data

def search_word(val,word):
    with open('BankChurners.csv', 'r',) as fbank:
        reader = csv.DictReader(fbank)
        for row in reader:
            if row[val].endswith(word):
                print(row)
                write_data(row)