import pandas as pd
def filter_val(colum,val):
    df = pd.read_csv("BankChurners.csv")
    sorted_df =df[colum] == val
    df[sorted_df].to_csv('filter_val.csv', index=False)
    print(df[sorted_df])

def filter_diap(colum,min,max):
    df = pd.read_csv("BankChurners.csv")
    sorted_df = (df[colum] > min) & (df[colum] < max)
    df[sorted_df].to_csv('filter_dip.csv', index=False)
    print(df[sorted_df])

def filter_letter(colum,letter):
    df = pd.read_csv("BankChurners.csv")
    sorted_df = df[colum].str.startswith(letter)
    df[sorted_df].to_csv('filter_letter.csv', index=False)
    print(df[sorted_df])

def filter_word(colum,word):
    df = pd.read_csv("BankChurners.csv")
    sorted_df = df[colum].str.contains(word)
    df[sorted_df].to_csv('filter_word.csv', index=False)
    print(df[sorted_df])
