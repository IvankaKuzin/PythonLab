import pandas as pd

def sort1(col,reg):
    df = pd.read_csv("BankChurners.csv")
    if reg==0:
        sorted_df = df.sort_values(by=[col], ascending=False)
    if reg==1:
        sorted_df = df.sort_values(by=[col], ascending=True)

    sorted_df.to_csv('sorted.csv', index=False)
    print(sorted_df)

def sort2(col1,col2, reg):
    df = pd.read_csv("BankChurners.csv")
    if reg == 0:
        sorted_df = df.sort_values(by=[col1,col2], ascending=False)
    if reg == 1:
        sorted_df = df.sort_values(by=[col1,col2], ascending=True)

    sorted_df.to_csv('sorted.csv', index=False)
    print(sorted_df)