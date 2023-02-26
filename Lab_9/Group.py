import pandas as pd

def group(col1,reg):
    df = pd.read_csv('BankChurners.csv')
    group = df[[col1]]
    print(group)
    group.to_csv('group_data.csv', index=False)
    if reg=='мінімальне':
        reg_min=group.min()
        print('Мінімальне значення: ',reg_min)
    if reg=='максимальне':
        reg_min=group.max()
        print('Максимальне значення: ',reg_min)
    if reg=='середнє':
        reg_min=group.mean()
        print('Середнє значення: ',reg_min)
    if reg=='відхилення':
        reg_min=group.std()
        print('Відхилення: ',reg_min)
