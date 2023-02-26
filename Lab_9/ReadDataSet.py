import pandas as pd
def read():
    csv_data=pd.read_csv('BankChurners.csv')
    print(csv_data)
    csv_data.to_csv('read.csv', index=False)
